//prime number generator
function generatePrimes(startReporting)
{
    let allPrimes = []
    let counter = 2 //where to start looking for primes
    let report = false //a toggle that turns on when looking at values greater than startReporting
    while(true)
    {
        //turn on reporting after certian number
        if (!report && counter > startReporting) {report = true} 

        let isNewPrime = true; //assume prime by default
        //if it is not divisible by prime numbers less than it, it is prime
        for(prime of allPrimes)
        {
            if(counter % prime == 0) 
            {
                isNewPrime = false; //not prime, no need to check more
                break
            }
        }

        //if it is a new prime number, print it and add it to known primes
        if(isNewPrime)
        {
            if(report) { console.log(counter) }
            allPrimes.push(counter);
        }

        //check next number
        counter++
    }
}

function identifyPrimeFactors(num)
{
    let start = new Date() //start timer

    //start trying to divide it by numbers until all factors divided out
    let primeFactors = []
    let checker = 2;
    while(num > 1)
    {
        if (num % checker == 0)
        {
            primeFactors.push(checker)
            num /= checker
        }
        else { checker++ }
    }
    console.log(primeFactors)

    let end = new Date() //end timer
    let timeTaken = end.getTime() - start.getTime()
    console.log('took ' + timeTaken + ' milliseconds')
    console.log('--------------------')
}


generatePrimes(1000000000) //uncomment to generate test data
//Create a program that:
//Lists all prime factors of: 35
//Lists all prime factors of: 120
//Lists all prime factors of: 13408723
//List all prime factors of: 4126159002481
//list all prime factors of: 113504942224931
identifyPrimeFactors(35)
identifyPrimeFactors(120)
identifyPrimeFactors(13408723)
identifyPrimeFactors(4126159002481)
identifyPrimeFactors(113504942224931)