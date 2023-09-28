ideologies = ("totalist", "radical_socialist", "social_democrat",
              "social_liberal", "market_liberal", "social_conservative",
              "authoritarian_democrat", "paternal_autocrat", "national_populist",
              "futurist", "corporatocratic", "theocratic")

ideologies_group_of_people = ("Totalists", "Radical socialists", "Social democrats",
                              "Social liberals", "Market liberals", "Social conservatives",
                              "Authoritarian democrats", "Paternal autocrats", "National populists",
                              "Futurists", "Corporatocrats", "Theocrats")

def generate_adding_removing_coalitions():
    for i in ideologies:
        print("add_" + i + "_to_coalition = {")
        print("\thidden_effect = {")
        print("\t\tset_temp_variable = { coalition_partner_var = token:" + i + " }")
        print("\t\tadd_to_coalition = yes")
        print("\t}")
        print("\tcustom_effect_tooltip = " + i + "_will_join_coalition_tt")
        print("}")
        print()
    print()
    for i in ideologies:
        print("remove_" + i + "_from_coalition = {")
        print("\thidden_effect = {")
        print("\t\tset_temp_variable = { coalition_partner_var = token:" + i + " }")
        print("\t\tremove_from_coalition = yes")
        print("\t}")
        print("\tcustom_effect_tooltip = " + i + "_will_leave_coalition_tt")
        print("}")
        print()


def generate_adding_removing_coalitions_tooltips():
    j = 0
    for i in ideologies:
        print (" " + i + "_will_join_coalition_tt: \"§B" + ideologies_group_of_people[j] + " will join our coalition§!\"")
        j += 1
    print()
    j = 0
    for i in ideologies:
        print (" " + i + "_will_leave_coalition_tt: \"§R" + ideologies_group_of_people[j] + " will leave our coalition§!\"")
        j += 1