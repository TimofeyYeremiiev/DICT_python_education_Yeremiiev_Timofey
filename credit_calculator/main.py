from credit_calculator import CreditCalculator
import argparse


calculator = CreditCalculator()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', default="annuity")
    parser.add_argument('--principal', '-pr')
    parser.add_argument('--periods', '-pe')
    parser.add_argument('--payment', '-pa')
    parser.add_argument('--interest', '-i')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(namespace)
    if True:
        if namespace.payment and namespace.periods:
            raise TypeError("Not combineability")
        match namespace.type:
            case "annuity":
                if namespace.principal:
                    calculator.set_credit_summ(namespace.principal)
                if namespace.periods:
                    calculator.set_months(namespace.periods)
                if namespace.interest:
                    calculator.set_percent(namespace.interest)
                if namespace.payment:
                    calculator.set_payment(namespace.payment)
                calculator.calc_au_credit()
                print(f"Overpay: {calculator.get_overpayment()}")
            case "diff":
                if namespace.principal:
                    calculator.set_credit_summ(namespace.principal)
                if namespace.periods:
                    calculator.set_months(namespace.periods)
                if namespace.interest:
                    calculator.set_percent(namespace.interest)
                if namespace.payment:
                    print("Parameter payment will be ignore for diff type")
                calculator.calc_di_credit()
                print(f"Overpay: {calculator.get_overpayment()}")
            case _:
                print("Type error")

