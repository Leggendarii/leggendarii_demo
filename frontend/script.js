async function calculate() {

    const voltage = document.getElementById("voltage").value;
    const power = document.getElementById("power").value;
    const ssc = document.getElementById("ssc").value;
    const xr = document.getElementById("xr").value;
    const frequency = document.getElementById("frequency").value;


    const response = await fetch(
        "http://127.0.0.1:8000/calculate",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                voltage: Number(voltage),
                power: Number(power),
                ssc: Number(ssc),
                xr: Number(xr),
                frequency: Number(frequency)
            })
        }
    );


    const data = await response.json();


    document.getElementById("scr").innerHTML = data.scr;
    document.getElementById("z").innerHTML = data.z;
    document.getElementById("r").innerHTML = data.r;
    document.getElementById("x").innerHTML = data.x;

}