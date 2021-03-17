package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_find_view_test.*
import kotlinx.android.synthetic.main.findview_exam.*

class FindViewTestActivity2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_find_view_test)
        btn_dream1.setOnClickListener{
            Toast.makeText(this,"android...start...1",Toast.LENGTH_LONG).show()
        }
        btn_dream2.setOnClickListener {
            Toast.makeText(applicationContext,"android...start...2",Toast.LENGTH_LONG).show()
        }
        var mylistener = object: View.OnClickListener{
            override fun onClick(v: View?) {
                Toast.makeText(applicationContext, "android...start...3",Toast.LENGTH_LONG).show()
            }
        }
        btn_Click.setOnClickListener(mylistener)
    }
}