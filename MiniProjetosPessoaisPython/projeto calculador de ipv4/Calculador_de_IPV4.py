import re


class CalculadorIPV4:
    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

    @property
    def network(self):
        return self._set_network()

    @property
    def broadcast(self):
        return self._set_broadcast()

    @property
    def number_ips(self):
        return self._get_number_of_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @ip.setter
    def ip(self, value):
        if not self._valida_ip(value):
            raise ValueError('Invalid IP')

        self._ip = value
        self._bin_ip = self._binary_ip(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._valida_ip(value):
            raise ValueError('Invalid Mask')

        self._mask = value
        self._bin_mask = self._binary_ip(value)
        self._prefix = sum([int(x) for x in ''.join(self._bin_mask)], start=0)

    @ prefix.setter
    def prefix(self, value):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError('Prefix must be a Integer')

        if value > 32:
            raise TypeError('Prefix must have 32-bits')

        self._prefix = value
        self._bin_mask = re.split(r'([0-1]{8})', f'{value* "1":0<32}')
        self._mask = self._bin_to_ip(self._bin_mask)

    @ staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')
        return regexp.search(ip)

    @ staticmethod
    def _bin_to_ip(bin_ip):
        add = 0
        ip = ''
        for octet in bin_ip:
            length = len(octet) - 1
            for num in octet:
                num = int(num)
                add += num*2**length
                length -= 1
                if length < 0:
                    ip += f'{add} '
                    add = 0
        return ip.strip().replace(' ', '.')

    @ staticmethod
    def _decimal_to_binary(num_ip):
        num_ip = int(num_ip)
        binary_string = ''

        while num_ip // 2 != 0:
            binary_string += str(num_ip % 2)
            num_ip = num_ip // 2

        binary_string += str(num_ip % 2)

        return f'{binary_string[::-1]:0>8}'

    @ staticmethod
    def _separate_ip(ip):
        return re.findall(r'\d+', ip)

    def _binary_ip(self, value):
        return [self._decimal_to_binary(i) for i in self._separate_ip(value)]

    def _set_broadcast(self):
        host_bits = 32 - self.prefix

        self._bin_broadcast = ''.join(self._bin_ip)[
            :self.prefix] + (host_bits * '1')

        self._broadcast = self._bin_to_ip(
            re.split(r'([0-1]{8})', self._bin_broadcast))

        return self._broadcast

    def _set_network(self):
        host_bits = 32 - self.prefix

        self._bin_network = ''.join(self._bin_ip)[
            :self.prefix] + (host_bits * '0')

        self._network = self._bin_to_ip(
            re.split(r'([0-1]{8})', self._bin_network))
        return self._network

    def _get_number_of_ips(self):
        return 2 ** (32 - self.prefix)


if __name__ == '__main__':
    pass
