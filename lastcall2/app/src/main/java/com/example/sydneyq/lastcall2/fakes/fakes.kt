package com.example.sydneyq.lastcall2.fakes

import com.example.sydneyq.lastcall2.api.models.BarData
import com.example.sydneyq.lastcall2.api.models.DrinkData

inline fun <reified T> toArray(list: List<*>): Array<T> {
    return (list as List<T>).toTypedArray()
}
/*
fun generateFakeBars(len: Int): Array<BarData> {

    var faker = Faker()
    return toArray((0..len).map {
        BarData(faker.idNumber().toString(),
                faker.name().toString(),
                faker.address().fullAddress().toString(),
                faker.number().numberBetween(1,5).toString(),
                faker.number().numberBetween(1,5),
                "${faker.address().latitude().toString()},${faker.address().longitude().toString()}",
                toArray((0..len).map {
                    DrinkData(
                            faker.name().toString(),
                            faker.number().numberBetween(5, 15).toFloat(),
                            faker.number().numberBetween(5, 40),
                            emptyArray())
                }
                ))
    })
}*/