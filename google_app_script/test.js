var t0 = performance.now()
for(i = 0; i < 1000000; i++)
{
    i = i + i
}
var t1 = performance.now()

console.log(t1-t0)