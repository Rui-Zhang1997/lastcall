package com.example.sydneyq.lastcall2.api.rest;

import com.example.sydneyq.lastcall2.api.models.BarHopMeta;
import com.example.sydneyq.lastcall2.api.models.Hop;
import com.example.sydneyq.lastcall2.api.models.HopMember;

import java.util.Date;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface LastCallRESTService {
    @POST("hop/make")
    Call<BarHopMeta> createNewHop(
            @Body String start,
            @Body String end,
            @Body String name,
            @Body Date stime,
            @Body int duration);

    @PUT("hop/{hopcode}/member")
    Call<Boolean> addMember(
            @Path("hopcode") String hopCode,
            @Body HopMember member);

    @GET("hop/join/{hopcode}")
    Call<BarHopMeta> joinHop(@Path("hopcode") String hopcode);

    @GET("hop/member/{id}")
    Call<HopMember> getMember(@Path("id") String id);

    @GET("hop/{hopId")
    Call<Hop> getHop(@Path("hopId") String hopId);
}

