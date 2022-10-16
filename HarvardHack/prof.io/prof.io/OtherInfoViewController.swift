//
//  OtherInfoViewController.swift
//  prof.io
//
//  Created by William Lee on 2022/10/15.
//

import UIKit

class OtherInfoViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        
    }
    
    @IBAction func apllyButton(_ sender: Any) {
        return
    }
    
    @IBAction func backButton(_ sender: Any) {
        self.performSegue(withIdentifier: "back3", sender: nil)
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
