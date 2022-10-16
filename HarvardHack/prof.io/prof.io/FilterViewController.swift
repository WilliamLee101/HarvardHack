//
//  FilterViewController.swift
//  prof.io
//
//  Created by William Lee on 2022/10/15.
//

import UIKit

class FilterViewController: UIViewController {
    
    
    
    @IBOutlet weak var loc_filter_text: UITextField!
    @IBOutlet weak var sub_filter_text: UITextField!
    @IBOutlet weak var Inp_filter_text: UITextField!
    
    
    var location_filter: String = ""
    var subject_filter: String = ""
    var InPerson_filter: Bool = false

    override func viewDidLoad() {
        super.viewDidLoad()
        loc_filter_text.text?.removeAll()
        sub_filter_text.text?.removeAll()
        Inp_filter_text.text?.removeAll()
    }
    
    @IBAction func backButton(_ sender: Any) {
        self.performSegue(withIdentifier: "back2", sender: nil)
    }
    
    
    @IBAction func filterButton(_ sender: Any) {
        location_filter = loc_filter_text.text!
        subject_filter = sub_filter_text.text!
        if (Inp_filter_text.text == "Yes"){
            InPerson_filter = true
        }else{
            InPerson_filter = false
        }
        return
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
