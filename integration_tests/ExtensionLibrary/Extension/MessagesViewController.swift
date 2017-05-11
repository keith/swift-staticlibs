import Dependency
import Messages
import UIKit

final class MessagesViewController: MSMessagesAppViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        Dependency.doStuff()
    }
}
