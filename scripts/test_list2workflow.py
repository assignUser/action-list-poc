import list2workflow as l2
def test_all():
    l = l2.load_list("list.yaml")
    wf = l2.generate_workflow(l)

    with open(".github/workflows/dummy.yml", "w") as file:
        file.write(wf)
