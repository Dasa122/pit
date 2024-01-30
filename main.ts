let num = 1
let num2 = 1
datalogger.deleteLog()
basic.forever(function () {
    let Páratlanszám: number[] = []
    let Négyzetszám: number[] = []
    Négyzetszám.push(num * num)
    Páratlanszám.push(num2)
    datalogger.log(
    datalogger.createCV("Négyzetszám", num * num),
    datalogger.createCV("Páratlanszám", num2)
    )
    num += 1
    num2 += 2
    basic.pause(1000)
})
basic.forever(function () {
	
})
