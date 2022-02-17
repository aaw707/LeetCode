class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x_bin = self.convert_to_binary(x)
        y_bin = self.convert_to_binary(y)

        x_bin_digit_num = len(x_bin)
        y_bin_digit_num = len(y_bin)

        distance_counter = 0

        if x_bin_digit_num > y_bin_digit_num:

            for i in range(0, x_bin_digit_num - y_bin_digit_num):
                if x_bin[i] == 1:
                    distance_counter += 1
            for j in range(0, y_bin_digit_num):
                if x_bin[x_bin_digit_num - y_bin_digit_num + j] != y_bin[j]:
                    distance_counter += 1

        elif x_bin_digit_num < y_bin_digit_num:

            for i in range(0, y_bin_digit_num - x_bin_digit_num):
                if y_bin[i] == 1:
                    distance_counter += 1
            for j in range(0, x_bin_digit_num):
                if y_bin[y_bin_digit_num - x_bin_digit_num + j] != x_bin[j]:
                    distance_counter += 1
        
        else:
            for i in range(0, x_bin_digit_num):
                if x_bin[i] != y_bin[i]:
                    distance_counter += 1
        
        return distance_counter


        
    def convert_to_binary(self, num):
        if num < 2:
            return [num % 2]

        binary_digits = self.convert_to_binary(num // 2)
        binary_digits.append(num % 2)

        return binary_digits
