//
//  ProfessorListViewController.swift
//  prof.io
//
//  Created by William Lee on 2022/10/15.
//

import UIKit
import FirebaseDatabase


class ProfessorListViewController: UIViewController {
    
    private let database = Database.database().reference()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        database.child("students").observe(.value) { snapshot in
            guard let value = snapshot.value as? [String: Any] else{
                return
            }
            
            print("Value: \(value)")
        }
        
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
