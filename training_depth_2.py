import training as tr

# tr.train(2, 10, 1, 1)
# tr.train(2, 10, 2, 0.1)
# tr.train(2, 10, 3, 0.01)
# tr.train(2, 10, 4, 0.001)
# tr.train(2, 10, 5, 0.0001)
# tr.train(2, 10, 6, 0.00001)
# tr.train(2, 10, 7, 0.000001)
# tr.train(2, 10, 8, 0.0000001)
# tr.train(2, 10, 9, 0.00000001)
# tr.train(2, 10, 10, 0.000000001)
# tr.train(2, 10, 11, 0.0000000001)
# tr.train(2, 10, 12, 0.00000000001)
# tr.train(2, 10, 13, 0.000000000001)

tr.train(2, 10, [x for x in range(1, 14)], 0)