import subprocess

import re


class StrReprMixin:
    """
    Enable you to Run your own command as
    if you were in cmd.
    Just print the Object.
    """

    def __str__(self):
        params = self._run_command()
        return params

    def __repr__(self):
        return self.__str__()


class Cmd(StrReprMixin):
    def __init__(self):
        """
        Shows easy-to-view IPv4.
        """
        self.ip = f'\n\033[1;35mIPv4:\033[1;37m{self._get_ip()}\033[m\n'

        """
        Get the wi-fi's SSID and Password in a list
        Recomend using for to the easy-to-view format.
        """
        self.wifis_data = self._get_wifi_data()

    @staticmethod
    def _wifi_profiles() -> str:
        """
        Return the command "netsh wlan show profiles" output in a string.
        """
        return subprocess.run(
            ['netsh', 'wlan', 'show', 'profiles'],
            capture_output=True).stdout.decode('ISO-8859-1')

    @ staticmethod
    def _ipconfig() -> str:
        """
        Return the command "ipconfig" output.
        """
        return subprocess.run(['ipconfig'],
                              capture_output=True).stdout.decode('ISO-8859-1')

    @staticmethod
    def _get_password(wifi_name) -> str:
        """
        Return the wi-fi's correspondent password.
        """
        return re.findall(r'Conte.+do da Chave .+: (.*)\r',
                          subprocess.run(
                              ['netsh', 'wlan', 'show',
                               'profile', wifi_name, 'key=clear'],
                              capture_output=True).stdout
                          .decode('ISO-8859-1'), flags=re.I)[0]

    def _run_command(self) -> str:
        """
        Run your command and return it's output.
        """
        try:
            return subprocess.run(input('Digite o comando: ').split(' '),
                                  capture_output=True).stdout.decode('ISO' +
                                                                     '-8859-1')
        except Exception:
            print('Unnable to run this command')
            return self._run_command()  # Calls this function to you again.

    def _wifi_name_list(self) -> list:
        """
        Return all wi-fi's SSID from profiles.
        """
        return re.findall(r'todos os perfis de usu.+rios: (.*)\r',
                          self._wifi_profiles(),
                          flags=re.I)

    def _get_ip(self) -> str:
        """
        Return Machine's IPv4 in str.
        """
        return re.findall(r'Endere.+ ipv4.*:(.*)\r',
                          self._ipconfig(), flags=re.I)[0]

    def _get_wifi_data(self) -> list:
        """
        Return wi-fi's profile SSID and Password in a list.
        """
        wifi_data_list = []
        for wifi in self._wifi_name_list():
            wifi_data_list.append(
                f'\n\033[1;35mSSID\033[m: \033[1;37m{wifi}\033[m\n' +
                '\033[1;35mPassword\033[m: ' +
                f'\033[1;37m{self._get_password(wifi)}\033[m\n')
        return wifi_data_list


if __name__ == '__main__':
    cmd = Cmd()
    print(cmd)
