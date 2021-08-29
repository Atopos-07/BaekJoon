import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = fib(n-1) + fib(n-2)
        return temp

def fib_dp_tb(n):
    fib_arry = [0, 1]
    def fib_dp_tb_temp(n):
        if n < len(fib_arry):
            return fib_arry[n]
        else:
            temp = fib_dp_tb_temp(n-1) + fib_dp_tb_temp(n-2)
            fib_arry.append(temp)
            return temp
    return fib_dp_tb_temp(n)

def fib_dp(n):
    fib_arry = [0, 1]
    def fib_dp_temp(n):
        if n < len(fib_arry):
            return fib_arry[n]
        else:
            while n >= len(fib_arry):
                temp = fib_arry[-1] + fib_arry[-2]
                fib_arry.append(temp)
            return fib_arry[n]
    ans = fib_dp_temp(n)
    return ans


def test_mean(fib_num=int,try_num=int,use_func=str):
    print(f"find fibonacci numbers : {fib_num}, try case : {try_num} time's")
    ans_arry = []
    time_arry = []
    print("runing : 0.00%", end="\r")
    for i in range(try_num):
        start = time.time()
        ans = use_func(fib_num)
        end = time.time() - start
        ans_arry.append(ans)
        time_arry.append(end)
        print(f"runing : {((i+1)/try_num)*100:.2f}%", end='\r' ,flush=True)
    for i in range(len(time_arry)):
        print(f"test case #{i} = ans : {ans_arry[i]}, time : {time_arry[i]:.10f}")
    print(f"mean : {sum(time_arry)/len(time_arry):.10f}")

def main():
    fib_num = 100
    try_num = 10
    use_func = fib_dp
    test_mean(fib_num, try_num, use_func)

def test():
    print(fib_dp(10))

main()
# test()