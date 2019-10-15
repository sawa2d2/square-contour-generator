import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#import os
#import subprocess

import benchmarks #ベンチマークのクラス
from mpl_toolkits.mplot3d import axes3d #明示的には使わないが、インポートしておく必要がある。

def show_graph(X, Y, Z, filename):
    fig = plt.figure(figsize=(8.72,6.99), dpi=100)
    ax = fig.gca(projection='3d')
    config = ax.plot_surface(X, Y, Z,
                             cmap=plt.cm.viridis, #色
                             linewidth=0)
    plt.colorbar(config)
    filename = filename + ".png"
    plt.tight_layout()

    plt.xlim([-interval, interval]) #x軸の描画範囲
    plt.ylim([-interval, interval]) #y軸の描画範囲
    plt.xticks([-interval, -interval/2, 0, interval, interval/2]) #x軸の刻み幅
    plt.yticks([-interval, -interval/2, 0, interval, interval/2]) #y軸の刻み幅

    plt.savefig(filename, #画像名
                bbox_inches='tight', #余白を小さく
                pad_inches=0.0, #余白の設定
    )
    #os.system("svg2emf " + filename)
    #plt.show()

def show_overview(Z):
    fig = plt.figure()
    plt.imshow(Z)
    plt.tight_layout()
    plt.savefig("overview.png", #画像名
                bbox_inches='tight', #余白を小さく
                pad_inches=0.0, #余白の設定
    )
    #plt.show()

def show_clabel(X, Y, Z, filename):
    border_num = 16
    border_width = 5.0
    fig = plt.figure(figsize=(26.48, 26.655), dpi=100)
    plt.contourf(X, Y, Z,
                 border_num, #等高線の本数
                 alpha=1.0, #アルファ値
                 cmap=plt.cm.viridis, #色
    )
    plt.contour(X, Y, Z,
                border_num,
                colors='#222222',
                linewidths=border_width,
    ) #境界線を表示
    plt.xticks(()) #x目盛りを非表示
    plt.yticks(()) #y目盛りを非表示

    #画像を出力
    filename = filename + "." + "png"
    plt.savefig(filename, #画像名
                bbox_inches='tight',
                pad_inches=-0.054, #余白の設定
                #transparent=True
    )
    #plt.show()
        
if __name__ == "__main__":
    benchmarks = benchmarks.benchmarks() #ベンチマーク呼び出し用
    interval = 5.12 #範囲
    stride = 600 #刻み幅
    plt.rcParams["font.size"] = 18 #文字サイズ

    plt.xlim([-interval, interval]) #xの描画範囲
    plt.ylim([-interval, interval]) #yの描画範囲
    plt.xticks([-interval, interval, interval / 2])
    plt.yticks([-interval, interval, interval / 2])
    plt.xlabel("x_1")
    plt.ylabel("x_2")
    x = np.arange(-interval, interval, interval / stride)
    y = np.arange(-interval, interval, interval / stride)

    X, Y = np.meshgrid(x, y)
    
    function_name = "griewank"

    if function_name == "sample":
        Z = benchmarks.sample(X, Y)
    if function_name == "sphere":
        Z = benchmarks.sphere(X, Y)
    if function_name == "rosenbrock":
        Z = benchmarks.rosenbrock(X, Y)
    if function_name == "rastrigin":
        Z = benchmarks.rastrigin(X, Y)
    if function_name == "griewank":
       Z = benchmarks.griewank(X, Y)
    if function_name == "ackley":
        Z = benchmarks.ackley(X, Y)
    if function_name == "gauss":
        Z = benchmarks.gauss(X, Y)

    filename = function_name + "contour"
    #show_graph(X, Y, Z, filename) #全体
    #show_overview(Z) #上から
    show_clabel(X, Y, Z, filename) #等高線
