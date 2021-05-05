# Function to find the maximum no.in a given array.
def DAC_Max(a, index, l):
    max = -1;
    if (index >= l - 2):
        if (a[index] > a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
    # Logic to find the Maximum element
    # in the given array.
    max = DAC_Max(a, index + 1, l);
    if (a[index] > max):
        return a[index];
    else:
        return max;
# Function to find the minimum no.in a given array.
def DAC_Min(a, index, l):
    min = 0;
    if (index >= l - 2):
        if (a[index] < a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
    # Logic to find the Minimum element in the given array.
    min = DAC_Min(a, index + 1, l);
    if (a[index] < min):
        return a[index];
    else:
        return min;
if __name__ == '__main__':
    min, max = 0, -1;
    a = [70, 250, 50, 80, 140, 12, 14];
    max = DAC_Max(a, 0, 7);
    min = DAC_Min(a, 0, 7);
    print("array is:",a);
    print("The minimum number in a given array is : ", min);
    print("The maximum number in a given array is : ", max);