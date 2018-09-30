package com.example.sydneyq.lastcall2.activities.viewhop

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import android.view.MotionEvent
import com.example.sydneyq.lastcall2.R
import com.mancj.slideup.SlideUp
import com.mancj.slideup.SlideUpBuilder
import com.mapbox.mapboxsdk.Mapbox
import io.reactivex.subjects.AsyncSubject
import io.reactivex.subjects.PublishSubject
import kotlinx.android.synthetic.main.activity_hop_view.*

class HopView : AppCompatActivity() {
    val slideUpDisposable = AsyncSubject.create<Float>()
    val slideDownLimit = 100f
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_hop_view)
        Mapbox.getInstance(this, "pk.eyJ1IjoicnoxODciLCJhIjoiY2o3dXZpZzR1NGJwNzJ3bzZ4cGo1b3cxMiJ9.e9NJyxQ8IXckHfWPPAhlOQ");
        mapView.onCreate(savedInstanceState)
    }
}
