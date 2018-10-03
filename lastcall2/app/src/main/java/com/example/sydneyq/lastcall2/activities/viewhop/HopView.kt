package com.example.sydneyq.lastcall2.activities.viewhop

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v4.app.ListFragment
import android.util.Log
import android.view.Gravity
import android.view.MotionEvent
import com.example.sydneyq.lastcall2.R
import com.example.sydneyq.lastcall2.api.models.HopMember
import com.example.sydneyq.lastcall2.api.rest.lastCallREST
import com.example.sydneyq.lastcall2.fragments.SlideUpListFragment
import com.mancj.slideup.SlideUp
import com.mancj.slideup.SlideUpBuilder
import com.mapbox.mapboxsdk.Mapbox
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.AsyncSubject
import io.reactivex.subjects.PublishSubject
import kotlinx.android.synthetic.main.activity_hop_view.*


class HopView : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_hop_view)
        Mapbox.getInstance(this, "pk.eyJ1IjoicnoxODciLCJhIjoiY2o3dXZpZzR1NGJwNzJ3bzZ4cGo1b3cxMiJ9.e9NJyxQ8IXckHfWPPAhlOQ");
        mapView.onCreate(savedInstanceState)
        val args = intent.extras.getBundle("args")
        val member = args.getSerializable("member") as HopMember
        if (member == null) {
            Log.e("HOPVIEW", "MEMBER IS NULL");
        } else {
            Log.e("HOPVIEW", member.toString())
        }
        lastCallREST.getHop(member.currentHop)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe { hop ->
                    Log.e("HOPRESULT", "HOP" + hop.toString())
                    val listFragment = SlideUpListFragment()
                    val args = Bundle()
                    args.putSerializable("bars", hop.bars)
                    args.putInt("type", 0)
                    listFragment.arguments = args
                    val fragmentManager = this.supportFragmentManager
                    val transaction = fragmentManager.beginTransaction()
                    transaction.replace(R.id.slide_up_fragment, listFragment)
                    transaction.addToBackStack(null)
                }
    }
}
