package com.example.sydneyq.lastcall2.api.models

import com.google.gson.annotations.SerializedName
import java.io.Serializable
import java.util.*

enum class Crowdedness {
    EMPTY, MODERATE, CROWDED
}

enum class Tolerance {
    LIGHTWEIGHT, MODERATE, LOTS
}

data class BarHopMeta(
        val hopId: String? = null,
        var hopName: String,
        var creatorName: String,
        var saddr: String,
        var eaddr: String,
        var stime: Date,
        var drunkLevel: Int,
        var barCount: Int,
        var maxBarCost: Int) : Serializable

data class HopMember(
        @SerializedName("_id") val memberId: String? = null,
        @SerializedName("creatorName") var memberName: String,
        var drunkLevel: Int,
        @SerializedName("maxBarCost") var maxCost: Int,
        // var crowdSize: Crowdedness,
        @SerializedName("hopId") var currentHop: String) : Serializable

data class BarData(
        val barId: String,
        val barName: String,
        var barAddress: String,
        val barRating: String,
        val barCost: Int,
        val ll: String,
        val menu: Array<DrinkData>) : Serializable

data class DrinkData(
        val drinkName: String,
        val drinkCost: Float,
        val alcoholVol: Int,
        val incredients: Array<String>) : Serializable

data class Hop(val hopId: String,
               val bars: Array<BarData>) : Serializable
