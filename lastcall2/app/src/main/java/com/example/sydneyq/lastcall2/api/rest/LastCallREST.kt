package com.example.sydneyq.lastcall2.api.rest

import retrofit2.Retrofit

val BASE_URL = "http://10.0.2.2:5000"
var retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .build()

var lastCallREST: LastCallRESTService = retrofit.create(LastCallRESTService::class.java)