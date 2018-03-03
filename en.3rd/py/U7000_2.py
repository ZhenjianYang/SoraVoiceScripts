from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7000_2 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1F90",         # 03, 3
        "Function_4_4374",         # 04, 4
        "Function_5_4397",         # 05, 5
        "Function_6_6014",         # 06, 6
        "Function_7_90C3",         # 07, 7
        "Function_8_90F3",         # 08, 8
        "Function_9_912D",         # 09, 9
        "Function_10_91FA",        # 0A, 10
        "Function_11_ACF8",        # 0B, 11
        "Function_12_CAFB",        # 0C, 12
        "Function_13_D01E",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00#50W#20A...I'm so sorry, Kevin...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #1 op#A
        "\x07\x00#50W#25A...I failed as your mother...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2 op#A
        (
            "\x07\x00#50W#55A...but I'm so tired...\x01",
            "I'm so, so tired...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3 op#A
        "\x07\x00#50W#55A...At least this way...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #4 op#A
        (
            "\x07\x00#50W#60A...At least this way,\x01",
            "the two of us can...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #5
        "\x07\x0C#3S#30W...!!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS420._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS421._CH")
    OP_1D(0xB2)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #6
        (
            "\x07\x0C#30W*pant*...*pant*...\x02\x03",

            "...\x02\x03",

            "That dream again?\x02\x03",

            "Ugh... How long is it going to take before\x01",
            "it goes away?\x02\x03",

            "It had to happen on Rufina's big day, too...\x02\x03",

            "I was hoping I'd be able to stop worrying her\x01",
            "when I got older, but at this rate...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #7
        (
            "\x07\x0C#30WI'm sure she's plenty used to you worrying\x01",
            "her already.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #8
        "\x07\x0C#30W#3S...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #9
        (
            "\x07\x0C#30WO-Oh, it's you, Ries... Don't scare me like that!\x02\x03",

            "How long have you been in here?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 250, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #10
        (
            "\x07\x0C#30WFor a while.\x02\x03",

            "We're supposed to be cleaning the chapel today,\x01",
            "but you weren't getting up, so I came to check\x01",
            "on you.\x02\x03",

            "You seemed to be having a nightmare, though,\x01",
            "so I thought I'd wake you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #11
        (
            "\x07\x0C#30WO-Oh. Okay...\x02\x03",

            "Haha. Sorry, Ries. I was being a pain for you\x01",
            "again, wasn't I?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 250, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #12
        (
            "\x07\x0C#30WNo more than usual.\x02\x03",

            "You've been a loser since the day I met you.\x01",
            "I don't expect that to change any time soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #13
        (
            "\x07\x0C#30WOuch... Kick a guy while he's down,\x01",
            "why don'cha?\x02\x03",

            "Well, whatever. We don't want to be\x01",
            "late for breakfast on Rufina's big day.\x02\x03",

            "So let's go and get this done.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 250, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #14
        "\x07\x0C#30W...All right.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS422._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS423._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(35, 65, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #15
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #16
        "\x07\x0C#30WRufina?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(140, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #17
        "\x07\x0C#30WOh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(50, 160, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #18
        (
            "\x07\x0C#30WGood morning, you two.\x02\x03",

            "I wasn't expecting to see you here this early.\x01",
            "Are you on cleaning duty today?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #19
        "\x07\x0C#30WYes, but...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #20
        (
            "\x07\x0C#30WWh-What are you doing up so early?!\x02\x03",

            "You've got a long journey ahead of you!\x01",
            "You need plenty of sleep or you're gonna\x01",
            "be exhausted before you even get there!\x02\x03",

            "I mean, isn't Arteria ages away from here?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(35, 180, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #21
        (
            "\x07\x0C#30WWell, yes.\x02\x03",

            "Buuut I won't be able to offer my prayers\x01",
            "to Aidios here again for quite some time.\x02\x03",

            "So I decided to get up early and pray for\x01",
            "all the days I'm going to be missing, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #22
        "\x07\x0C#30W...Seriously? That's why?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #23
        (
            "\x07\x0C#30WHeehee. That's very you.\x02\x03",

            "Are you really going to be that busy, though?\x02\x03",

            "I thought you might be able to come home\x01",
            "from time to time, at least...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS424._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS425._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS426._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS427._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS428._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS429._CH")
    OP_C5(0x6, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS480._CH")
    OP_C5(0x7, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS481._CH")
    OP_C5(0x8, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS482._CH")
    OP_C5(0x9, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS483._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #24
        (
            "\x07\x0C#30WI wish I could say otherwise, but I probably will.\x02\x03",

            "I've only just become a squire, so there'll be\x01",
            "plenty of work in store for me. I'll be lucky\x01",
            "to find time to sleep, never mind come home.\x02\x03",

            "I might be able to squeeze some time into my\x01",
            "schedule once I've gotten the hang of the\x01",
            "workload, but until then...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #25
        "\x07\x0C#30WOkay...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #26
        (
            "\x07\x0C#30WAnd that's why you've gotta sleep now while\x01",
            "you still can!\x02\x03",

            "Come on! You've done enough praying for\x01",
            "one day, so go back to bed until breakfast\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #27
        "\x07\x0C#30W*sniffle* You're so cold to me...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(410, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #28
        "\x07\x0C#30W...Uhh, what? How?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(45, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #29
        (
            "\x07\x0C#30WI thought you'd want to make the most\x01",
            "of the time you've got left with me, but\x01",
            "it's like you don't even want me here...\x02\x03",

            "*sniffle* Did I do a bad job at raising you?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #30
        (
            "\x07\x0C#30WI-I never said I didn't want you here!\x02\x03",

            "And you might've done a lot for me,\x01",
            "but 'raising me' is a stretch!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #31
        (
            "\x07\x0C#30W...It's okay. He's just embarrassed.\x02\x03",

            "He's actually more than happy to talk\x01",
            "to you--he's just terrible at showing it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(400, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #32
        "\x07\x0C#30WOh, get over yourself!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #33
        (
            "\x07\x0C#30WIs that so, now?\x02\x03",

            "I should've known! You're such a typical boy,\x01",
            "Kevin.\x02\x03",

            "They all act indifferent to avoid letting their\x01",
            "loved ones know just how much they care.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(270, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #34
        (
            "\x07\x0C#30WAnd don't forget: he's at that rebellious age,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #35
        (
            "\x07\x0C#30W...How have I managed to survive being\x01",
            "twisted around your fingers for so long?\x02\x03",

            "Is trying to toy with the hearts of innocent\x01",
            "young boys a family thing, or what?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x5, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #36
        (
            "\x07\x0C#30WHeehee... Oh, I'd hardly say 'young.' It's been\x01",
            "about five years by now, you know.\x02\x03",

            "Ah! Speaking of which, I think I'm starting to\x01",
            "get a craving for some chocolate. Maybe I\x01",
            "should pick some up on the way to the station.\x02\x03",

            "Quincy Bell, of course. For obvious reasons.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(420, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #37
        "\x07\x0C#30W...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #38
        (
            "\x07\x0C#30WOh! Their new mint chocolate's my current\x01",
            "favorite.\x02\x03",

            "The fresh aftertaste mixes in with the\x01",
            "chocolate's flavor really well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #39
        (
            "\x07\x0C#30WI'll admit that does sound tempting, but I think\x01",
            "I'm more in the mood for the classic milk this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x6, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #40
        (
            "\x07\x0C#30WThat flavor will always be a fond little trip down\x01",
            "Memory Lane for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x7, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #41
        "\x07\x0C#30WBecause of how we met...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #42
        (
            "\x07\x0C#30W...\x02\x03",

            "Kevin, you're disgusting.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 0, 0)
    OP_C6(0x8, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #43
        "\x07\x0C#30W#3SWh-Why?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #44
        (
            "\x07\x0C#30WHeehee. I think we all get that warm and fuzzy\x01",
            "feeling when we look back on it.\x02\x03",

            "After all, the day you came to live with us, Kevin,\x01",
            "was the start of many, many new and wonderful\x01",
            "memories.\x02\x03",

            "I treasure every single one I've made during these\x01",
            "five years. They're all priceless to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #45
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #46
        (
            "\x07\x0C#30WThen...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x6, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #47
        (
            "\x07\x0C#30WThen why did you decide to become a squire and\x01",
            "leave us?\x02\x03",

            "It just doesn't seem like the right job for you...\x02\x03",

            "Even if you wanted to be in the church, couldn't \x01",
            "you have become a sister at the chapel in town\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #48
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS484._CH")
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #49
        (
            "\x07\x0C#30W...I'm sorry, Kevin.\x02\x03",

            "Apparently I've just got the aptitude for it,\x01",
            "or so I've been told.\x02\x03",

            "I feel like the best thing I can do is make use\x01",
            "of that and try to help people in the best way \x01",
            "I can.\x02\x03",

            "Of course, there's always the chance I won't\x01",
            "be cut out for it at all and will have to come\x01",
            "home anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x9, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #50
        (
            "\x07\x0C#30WHmph...\x02\x03",

            "There's no way a girl as naive as you is gonna be\x01",
            "any good with the kind of crazy-tough stuff you'd\x01",
            "have to do.\x02\x03",

            "You better come straight back home once you've\x01",
            "had enough!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #51
        "\x07\x0C#30W*nod*\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #52
        (
            "\x07\x0C#30WPffft. Really? Well, if it DOES come to that,\x01",
            "I'll be expecting a nice, warm welcome from\x01",
            "the two of you!\x02\x03",

            "And with that, I believe this conversation has\x01",
            "done a lovely job with helping you procrastinate\x01",
            "cleaning for long enough. Should I lend a hand?\x02\x03",

            "If we're going to do the job, we might as well do\x01",
            "it perfectly and have the whole chapel sparkling!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_AD(0x2400E5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_1F90(): pass

    label("Function_3_1F90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2602AD, 0x2602B2, 0x13)
    OP_D2(0x2602AC, 0x2602B1, 0x14)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x12, 0, 4000, -1770, 0)
    SetChrPos(0x109, -530, 4000, -2920, 0)
    SetChrPos(0x10F, -1180, 4000, -3890, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, 870, 4000, -4110, 0)
    SetChrPos(0x13, -1060, 4000, -5450, 0)
    SetChrPos(0x14, 1700, 4000, -5520, 0)
    SetChrPos(0x15, 200, 4000, -5060, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_210B():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_210B)

    def lambda_2123():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2123)

    def lambda_213B():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_213B)

    def lambda_214B():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_214B)
    OP_8F(0x12, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 100, 5100, 100, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_2234():
        OP_8F(0xFE, 0x64, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2234)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x12, 0, 4000, -490, 0)
    SetChrPos(0x109, -700, 4000, -2150, 0)
    SetChrPos(0x10F, -1450, 4000, -3000, 0)
    SetChrPos(0x11, 580, 4000, -3500, 0)
    SetChrPos(0x13, -1360, 4000, -4700, 0)
    SetChrPos(0x14, 1290, 4000, -4760, 0)
    SetChrPos(0x15, -60, 4000, -4150, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x10, 0, 5700, 1000, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2397():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2397)

    def lambda_23AF():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23AF)

    def lambda_23C7():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_23C7)

    def lambda_23D7():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_23D7)

    def lambda_23E7():
        OP_8F(0xFE, 0x0, 0x2008, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_23E7)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_2411():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2411)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 300, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    Sleep(300)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 0, 8000, 2800, 180)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x17, 0, 8000, 2800, 180)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    PlayEffect(0x6, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(500)

    def lambda_2581():
        OP_8F(0xFE, 0xFFFFFCE0, 0x1F40, 0xAF0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2581)

    def lambda_259C():
        OP_8F(0xFE, 0x3E8, 0x1F40, 0xAF0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_259C)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #53
        0x10F,
        "#1444F#5PTwo lights...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        "#1060F#5PHmm... I wonder if the other one could be...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x16, -500, 8000, 2150, 180)
    SetChrPos(0x17, 1000, 8000, 2150, 180)
    PlayEffect(0x6, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x12, 10, 4000, -490, 0)
    SetChrPos(0x109, -20, 4000, -2410, 0)
    SetChrPos(0x10F, -720, 4000, -3390, 0)
    SetChrPos(0x11, 1210, 4000, -4000, 0)
    SetChrPos(0x13, -660, 4000, -5230, 0)
    SetChrPos(0x14, 2290, 4000, -5300, 0)
    SetChrPos(0x15, 570, 4000, -4900, 0)

    def lambda_283E():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_283E)

    def lambda_2856():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2856)

    def lambda_286E():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_286E)

    def lambda_287E():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_287E)

    def lambda_288E():
        OP_8F(0xFE, 0xFFFFFF9C, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_288E)

    def lambda_28A9():
        OP_8F(0xFE, 0x320, 0xFA0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_28A9)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x6, 0x5, 0x16, 300, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x17, 0, 300, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2954():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2954)

    def lambda_2966():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2966)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_0D()
    Sleep(1000)
    PlayEffect(0x4, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_29FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_29FB)

    def lambda_2A0D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2A0D)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    Fade(500)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x17,
        "#310F#11PScree?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x16,
        "Princess Klaudia",
        "#1169F#5PWh-What just happened...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFF06, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x16, 1)
    OP_0D()
    Sleep(300)

    NpcTalk(    #57
        0x16,
        "Princess Klaudia",
        (
            "#1164F#5P...Julia?\x02\x03",

            "Did you not leave for a training exercise\x01",
            "on board the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#176F#6PI'm so relieved to see you safe, Your Highness...\x02\x03",

            "#171FHaha. I see Sieg is with you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x17,
        "#310F#11PScree?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x16,
        "Princess Klaudia",
        (
            "#1163F#5PHe is, but...umm...I'm not quite sure what's\x01",
            "going on...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFF06, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #61
        0x16,
        "Princess Klaudia",
        "#1164F#11PWha...?\x02",
    )

    CloseMessageWindow()

    def lambda_2C4D():
        OP_6D(-880, 4000, 300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C4D)

    def lambda_2C65():
        OP_67(0, 6060, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C65)

    def lambda_2C7D():
        OP_6B(2730, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C7D)
    OP_43(0x12, 0x0, 0x2, 0x4)
    Sleep(400)

    def lambda_2C99():
        OP_8F(0xFE, 0x0, 0xFA0, 0xFFFFFA60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C99)
    Sleep(200)

    def lambda_2CB9():
        OP_8F(0xFE, 0xFFFFFD44, 0xFA0, 0xFFFFF650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2CB9)
    Sleep(150)

    def lambda_2CD9():
        OP_8F(0xFE, 0x578, 0xFA0, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2CD9)
    Sleep(150)

    def lambda_2CF9():
        OP_8F(0xFE, 0x37A, 0xFA0, 0xFFFFF18C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2CF9)
    Sleep(150)

    def lambda_2D19():
        OP_8F(0xFE, 0x898, 0xFA0, 0xFFFFEF98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2D19)
    Sleep(150)

    def lambda_2D39():
        OP_8F(0xFE, 0xFFFFFE34, 0xFA0, 0xFFFFEF70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2D39)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x3)
    Sleep(500)

    ChrTalk(    #62
        0x109,
        "#1840F#6PHaha... Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#560F#6PHi, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x13,
        "#277F#6P...*nod*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "#210F#6PI... Uhh... I sure wasn't expecting to run\x01",
            "into you here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #66
        0x16,
        "Princess Klaudia",
        (
            "#1164F#11PWh-What are you all doing here...?\x02\x03",

            "#1382FO-Oh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x15,
        (
            "#1513F#6PIt's good to see you again, Kloe.\x02\x03",

            "#1501FAnd Sieg, too, of course. You two look well.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #68
        0x16,
        "Princess Klaudia",
        (
            "#1382F#11PTh-Thank you...\x02\x03",

            "#1165FAha... I'm not sure what to say...\x02\x03",

            "#1168FI feel like I should be waking up any moment\x01",
            "now, but I'm not sure I even want to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x17,
        "#311F#11PScree!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x16, 290, 4000, -190, 180)
    ClearChrFlags(0x16, 0x40)
    ClearChrFlags(0x16, 0x4)
    SetChrPos(0x17, -200, 4600, 50, 180)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x1)
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -870, 4000, -2950, 0)
    SetChrPos(0x11, 1260, 4000, -4600, 0)
    SetChrPos(0x12, 1550, 4000, -3380, 0)
    SetChrPos(0x13, -820, 4000, -5200, 0)
    SetChrPos(0x14, 2790, 4000, -5300, 0)
    SetChrPos(0x15, -150, 4000, -4400, 0)
    OP_6D(-1180, 4000, -600, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #70
        0x16,
        "Princess Klaudia",
        (
            "#1167F#11PI see...\x02\x03",

            "#1163FWe've found ourselves in quite the predicament,\x01",
            "haven't we?\x02\x03",

            "I'm relieved to hear that the empty Grancel you\x01",
            "found wasn't the real city, at least, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        (
            "#1446F#6PUnfortunately, that doesn't necessarily rule\x01",
            "out the real capital being in danger.\x02\x03",

            "#1443FWe're dealing with something that has such\x01",
            "great power, it can create a flawless replica\x01",
            "of a vast city.\x02\x03",

            "There's no telling how far its influence could\x01",
            "extend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        "#175F#12PRies...surely there is no need to worry her so?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #73
        0x16,
        "Princess Klaudia",
        (
            "#1167F#11PWe have nothing to gain from shying away from\x01",
            "the truth. If anything, she's helping me better\x01",
            "understand the gravity of the situation we're in.\x02\x03",

            "#1162FI'd like to help with the investigation if I can.\x02\x03",

            "I'm not sure I could do much more than what\x01",
            "you're already doing, but I won't drag you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x17,
        "#310F#5PScree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x12,
        "#178F#6PBut, Your Highness...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x16,
        "Princess Klaudia",
        (
            "#1167F#11PI'm sorry, Julia, but I'm afraid nothing you can\x01",
            "say will change my mind.\x02\x03",

            "#1382FI may not fully understand the situation we're in,\x01",
            "but I do know that it threatens the safety of our\x01",
            "capital--perhaps the whole nation.\x02\x03",

            "I'd be a disgrace as a crown princess if I were\x01",
            "to just stand by and do nothing while the people\x01",
            "I will one day rule over are threatened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x15,
        "#1500F#6PWow... You're amazing, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12,
        "#176F#6P...As you wish, Your Highness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        "#1840F#6PWell, welcome to the team.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x16,
        "Princess Klaudia",
        (
            "#1165F#11PGreat! I'll do what I can.\x02\x03",

            "#1162FSo, is our next destination that teleportation\x01",
            "circle at the end of the sealed area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1065F#6PYeah. That should let us travel to the next area.\x02\x03",

            "#1063FOr, by the sounds of it, to the next plane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x15,
        (
            "#1503F#6PYeah.\x02\x03",

            "#1502FThat appears to be the technical name for the\x01",
            "various areas that make up the land we're in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10F,
        (
            "#1446F#5PIt's a concept used in the Septian Church, too. \x01",
            "Our world is made up of a number of planes or \x01",
            "realms situated on top of one another.\x02\x03",

            "At the top is the sky where the Goddess dwells,\x01",
            "below that is the earth where we live, and at the\x01",
            "bottom lies Gehenna--where sinners are judged.\x02\x03",

            "#1443FThose are the main three, but in between them,\x01",
            "there are countless other planes or realms, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "#272F#6PHmm... So, in other words...\x02\x03",

            "#270F...the farther down we descend, the less\x01",
            "the blessings of the Goddess will be able\x01",
            "to reach us?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    def lambda_39FB():
        OP_6D(-900, 3700, -1600, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_39FB)
    OP_8C(0x14, 270, 600)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #85
        0x14,
        (
            "#216F#12PH-Hey! Can you not SAY stuff like that?\x02\x03",

            "#413FWith all the creepy monsters roaming around,\x01",
            "it's freaky enough around here as it is!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AB1():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3AB1)
    Sleep(50)

    def lambda_3AC4():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3AC4)
    Sleep(50)

    def lambda_3AD7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3AD7)
    Sleep(50)

    def lambda_3AEA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3AEA)
    Sleep(50)

    def lambda_3AFD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3AFD)
    Sleep(50)
    OP_8C(0x12, 135, 400)

    ChrTalk(    #86
        0x13,
        (
            "#278F#5PHeh. You sound like a child who's afraid to\x01",
            "walk around the house when the lights are\x01",
            "off.\x02\x03",

            "#277F...Although I suppose that does make sense,\x01",
            "given that you truly are a child.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0x14,
        "#214F#12P#3SI am SO not a child!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #88
        0x11,
        (
            "#067F#6PAhem! A-Anyway!\x02\x03",

            "#560FIf that fake Grancel was the second plane, \x01",
            "the next one's the third, right?\x02\x03",

            "I mean, it sounds obvious, but I'm not sure\x01",
            "it's all going in one clear direction or if we\x01",
            "might run into a fork at some point.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D36():
        OP_6D(-1200, 3700, -1000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3D36)

    def lambda_3D4E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D4E)
    Sleep(50)

    def lambda_3D61():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3D61)
    Sleep(50)

    def lambda_3D74():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3D74)
    Sleep(50)

    def lambda_3D87():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3D87)
    Sleep(50)

    def lambda_3D9A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3D9A)
    Sleep(50)
    OP_8C(0x14, 315, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(200)

    ChrTalk(    #89
        0x109,
        (
            "#1060F#11PI think straightforward is a safe enough assumption\x01",
            "to make for now.\x02\x03",

            "#1065FAnd while we might not know what that Lord of\x01",
            "Phantasma wants with us, we know it's nothing good.\x02\x03",

            "#1063FSo even if it's not like that, that doesn't change how\x01",
            "ugly this could get, so let's get ready for just about\x01",
            "anything. Who knows what's waiting for us up ahead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10F,
        "#1802F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x109,
        (
            "#1079F#11PHmm? Something wrong, Ries?\x02\x03",

            "If you think you might've figured something out,\x01",
            "the rest of the class would love to hear about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10F,
        (
            "#1446F#5PNo, it's nothing important.\x02\x03",

            "#1443FYou're right. We should start getting ready to\x01",
            "leave.\x02\x03",

            "It may be worth our while to investigate some\x01",
            "of the doors we've encountered thus far, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x14,
        (
            "#210F#6PYeah. I don't know what's up with those things,\x01",
            "but there sure are a ton of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x15,
        (
            "#1505F#6PAt the very least, they don't seem to have been\x01",
            "placed by any of our foes.\x02\x03",

            "#1500FI'm all in favor of investigating them, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4192():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4192)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2800)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2E, 0x1, 0x40)
    OP_28(0x2E, 0x1, 0x80)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x4, 0x20)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x4, 0x20)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x4, 0x20)
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x4, 0x20)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    OP_3F(0x357, 1)
    OP_DB(0x0, 0x4)
    OP_A2(0x25CA)
    Call(6, 14)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_1F90 end

    def Function_4_4374(): pass

    label("Function_4_4374")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFFA24, 0xFA0, 0xFFFFFDA8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_4374 end

    def Function_5_4397(): pass

    label("Function_5_4397")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DC(0x2, 0xFF)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(2000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #95
        (
            "\x07\x0C#30WKevin Graham, of the 543rd class of trainees...\x02\x03",

            "In the name of the Goddess above, I hereby \x01",
            "appoint you a squire of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xB2)
    OP_AD(0x240121, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #96
        (
            "\x07\x0C#30WI humbly accept my appointment.\x02\x03",

            "I pledge to offer my soul to the Goddess above,\x01",
            "and both body and blood to Her church on earth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 120, -1, -1)
    SetChrName("Congregation for the Sacraments Cardinal")

    AnonymousTalk(    #97
        (
            "\x07\x0C#30WVery good.\x02\x03",

            "It is exceedingly rare for one at your age to\x01",
            "be appointed to this position.\x02\x03",

            "I can only assume your aptitudes and training\x01",
            "achievements warranted it.\x02\x03",

            "May you strive to be a worthy guardian of the\x01",
            "Goddess' sacraments as Her loyal and devoted\x01",
            "servant.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_AE(0xC8)
    Sleep(3000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS434._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS435._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS436._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS437._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #98
        (
            "\x07\x0C#30WWell, if it isn't Kevin.\x02\x03",

            "I see you managed to avoid having your promotion\x01",
            "rejected by the top brass.\x02\x03",

            "Splendid, splendid.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #99
        (
            "\x07\x0C#30WInstructor...I really can't thank you enough for\x01",
            "all you've done for me.\x02\x03",

            "I never dreamed I would have an actual Dominion\x01",
            "supervising my training. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #100
        (
            "\x07\x0C#30WHeh. How sweet of you to say.\x02\x03",

            "Hard to believe you're the same boy who waltzed\x01",
            "up before the Congregation for the Sacraments\x01",
            "shouting, 'Make me a knight! Pleeease!'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #101
        (
            "\x07\x0C#30WHaha... I'd appreciate it if you'd chuck that\x01",
            "memory back into the furthest reaches of\x01",
            "your mind, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #102
        (
            "\x07\x0C#30WOh, but how could I? Had I missed your groveling,\x01",
            "I never would have taken an interest in you in the\x01",
            "first place.\x02\x03",

            "And not in a million years would I have thought\x01",
            "you were related to Rufina.\x02\x03",

            "You could have asked her to take you on as her\x01",
            "pupil before resorting to such drastic measures,\x01",
            "you silly boy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #103
        "\x07\x0C#30WW-Well...I had my reasons. Let's leave it at that.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #104
        (
            "\x07\x0C#30WHaha. Very well. It doesn't matter at this point,\x01",
            "anyway.\x02\x03",

            "Congratulations! You're now a dog of the church\x01",
            "just like the rest of us.\x02\x03",

            "It's good to have you on board.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #105
        (
            "\x07\x0C#30WThank you.\x02\x03",

            "I'm not sure that's the most reassuring metaphor\x01",
            "to be using on new recruits, though.\x02\x03",

            "You might scare some of 'em right off.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #106
        (
            "\x07\x0C#30WPlease. You're not trying to position yourself\x01",
            "as some sweet, doe-eyed thing, are you?\x02\x03",

            "Besides, I think it's a perfectly apt description\x01",
            "for us.\x02\x03",

            "We go around sniffing out sacraments wherever\x01",
            "they may be, tearing through the throats of the\x01",
            "heretical fools who are enamored with them all\x01",
            "the while.\x02\x03",

            "Can you spot the difference?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #107
        (
            "\x07\x0C#30WC'mon, Instructor. I'm used to you at this point,\x01",
            "so I don't really care if you call me a dog.\x02\x03",

            "But--\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #108
        (
            "\x07\x0C#30WBut you care if I call your beloved Rufina one,\x01",
            "don't you?\x02\x03",

            "Not to worry, Kevin. I can read between the\x01",
            "lines well enough.\x02\x03",

            "Well? Did I guess right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #109
        (
            "\x07\x0C#30WI-I owe her a lot, but I wouldn't call her my\x01",
            "'beloved'...\x02\x03",

            "She's just like a big sister to me, that's all.\x02\x03",

            "You're making it sound like I...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 380, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #110
        "\x07\x0C#30WLike you...what, exactly?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #111
        "\x07\x0C#30W#3S...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #112
        (
            "\x07\x0C#30WR-Rufina?!\x02\x03",

            "I-I thought you were in Remiferia on a mission!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #113
        (
            "\x07\x0C#30WHeehee. I was, but I tried to finish as\x01",
            "quickly as possible so I could be back\x01",
            "for your appointment ceremony.\x02\x03",

            "I'm so proud of you, Kevin!\x02\x03",

            "It's amazing just how fast you've grown... \x01",
            "Now you're a full-fledged adult like me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #114
        (
            "\x07\x0C#30WWow... Thanks for going out your way to\x01",
            "come here.\x02\x03",

            "I'm not sure I deserve to be called an adult\x01",
            "yet, though. \x02\x03",

            "I've got a whole lot of work ahead of me\x01",
            "if I want to be half the knight the two of\x01",
            "you are.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #115
        (
            "\x07\x0C#30WOh, my. How modest of you.\x02\x03",

            "By the way, have you let Ries know about all\x01",
            "of this yet?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #116
        (
            "\x07\x0C#30WNot yet. I'm planning to write to her tonight.\x02\x03",

            "She's been real mad at me ever since I decided\x01",
            "to come to Arteria, though...\x02\x03",

            "Hopefully this'll cheer her up a bit... There's not\x01",
            "much else I can do to make up with her short of\x01",
            "going home.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #117
        (
            "\x07\x0C#30WPerhaps we should do that together at some\x01",
            "point if we can find the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #118
        (
            "\x07\x0COh, and while I have the chance...thank you so\x01",
            "much for looking after him all this time, Ein.\x02\x03",

            "You've given up so much of your free time, and\x01",
            "I really do appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 320, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #119
        (
            "\x07\x0C#30WThink nothing of it. It proved quite a fun way\x01",
            "to kill time.\x02\x03",

            "He has a fair amount of potential in combat\x01",
            "arts and Thaumaturgy, too.\x02\x03",

            "It's a shame all his skills are on the practical\x01",
            "side of things, however. His academic side is...\x01",
            "less than stellar.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #120
        (
            "\x07\x0C#30W*sigh* I had this feeling in the pit of\x01",
            "my stomach that may be the case...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #121
        (
            "\x07\x0C#30WHaha...haha...\x02\x03",

            "Oh! Right! I've gotta get going!\x02\x03",

            "I have to pick up my new room key and \x01",
            "medal from the general affairs guys.\x02\x03",

            "Sorry! I'll talk to you later!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #122
        "\x07\x0C#30WOh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #123
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #124
        (
            "\x07\x0C#30WWhat's this? You look so concerned.\x02\x03",

            "Feeling guilty because he followed you\x01",
            "into such a dangerous line of work?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #125
        (
            "\x07\x0C#30WNot at all. That was completely up to him and\x01",
            "him alone. I would never try to dictate his life\x01",
            "choices.\x02\x03",

            "It's just that...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #126
        (
            "\x07\x0C#30WI think he'll make a fine knight, personally.\x02\x03",

            "He checks all the boxes; he's got the potential,\x01",
            "he's got the determination... All in all, I can see\x01",
            "why you're so proud of him.\x02\x03",

            "And... And call it a hunch, but...\x02\x03",

            "...I wouldn't be surprised if he...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #127
        (
            "\x07\x0C#30W...if a Stigma manifested in him just like it has\x01",
            "in you?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #128
        (
            "\x07\x0C#30WWell, I'm impressed. I didn't think you could sense\x01",
            "that of others if you didn't possess one yourself.\x02\x03",

            "Yet one more reason to feel frustrated that you\x01",
            "aren't a Dominion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #129
        (
            "\x07\x0C#30WHaha... I know we're friends, but there's no need\x01",
            "for all the flattery.\x02\x03",

            "My combat and Thaumaturgy abilities are average\x01",
            "at best. I wouldn't be cut out for the job at all.\x02\x03",

            "I'm grateful enough to have been promoted from\x01",
            "squire to knight. That's the upper limit for someone\x01",
            "with my lack of potential.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #130
        (
            "\x07\x0C#30WIf only you saw things the way I do.\x02\x03",

            "Someone with 'average at best' abilities couldn't\x01",
            "have handled your Ouroboros case half as well as\x01",
            "you did.\x02\x03",

            "Fighting off a man of that reported strength to a\x01",
            "swift enough conclusion would be a pretty feather\x01",
            "in anyone's cap.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #131
        (
            "\x07\x0C#30WIt was just my luck that we both came to an\x01",
            "understanding.\x02\x03",

            "As far as Kevin goes, he wouldn't need to\x01",
            "rely on luck. His potential for growth extends\x01",
            "further than I'll ever be able to go.\x02\x03",

            "But he has one weakness holding him back.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Rufina")

    AnonymousTalk(    #132
        (
            "\x07\x0C#40W...That poor boy is just far too kind.\x02\x03",

            "So kind, in fact, that I can see him driving\x01",
            "himself into a corner because of it one day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_AD(0x2400E6, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2507)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_4397 end

    def Function_6_6014(): pass

    label("Function_6_6014")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270047, 0x27004C, 0x13)
    OP_D2(0x270048, 0x27004D, 0x14)
    OP_D2(0x70074, 0x7007C, 0x15)
    OP_D2(0x70075, 0x7007D, 0x16)
    OP_D2(0x260285, 0x26028A, 0x17)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x11, 1270, 4000, -2970, 0)
    SetChrPos(0x12, 1870, 4000, -5330, 0)
    SetChrPos(0x13, 430, 4000, -5710, 0)
    SetChrPos(0x14, 2830, 4000, -4170, 0)
    SetChrPos(0x16, 940, 4000, -4120, 0)
    SetChrPos(0x15, -840, 4000, -4250, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_61C3():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_61C3)

    def lambda_61DB():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_61DB)

    def lambda_61F3():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_61F3)

    def lambda_6203():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6203)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 23)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 400, 5300, 0, 0)
    SetChrChipByIndex(0x18, 19)
    SetChrSubChip(0x18, 0)
    PlayEffect(0x1, 0x0, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -400, 5300, 0, 0)
    SetChrChipByIndex(0x19, 21)
    SetChrSubChip(0x19, 0)
    PlayEffect(0x1, 0x2, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_63AF():
        OP_8F(0xFE, 0x190, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_63AF)

    def lambda_63CA():
        OP_8F(0xFE, 0xFFFFFE70, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_63CA)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x18, 400, 6000, 1000, 0)
    SetChrPos(0x19, -400, 6000, 1000, 0)

    def lambda_6484():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6484)

    def lambda_649C():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_649C)

    def lambda_64B4():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_64B4)

    def lambda_64C4():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_64C4)

    def lambda_64D4():
        OP_8F(0xFE, 0x3E8, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_64D4)

    def lambda_64EF():
        OP_8F(0xFE, 0xFFFFFC18, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_64EF)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_651E():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_651E)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x4, 0x18, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0x19, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x4, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x1, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x3, 0x19, 0, 0, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(500)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x19, 1000, 8000, 2150, 270)
    SetChrPos(0x18, -500, 8000, 2150, 90)
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x11, 1270, 4000, -2970, 0)
    SetChrPos(0x12, 1870, 4000, -5330, 0)
    SetChrPos(0x13, 430, 4000, -5710, 0)
    SetChrPos(0x14, 2830, 4000, -4170, 0)
    SetChrPos(0x16, 940, 4000, -4120, 0)
    SetChrPos(0x15, -840, 4000, -4250, 0)

    def lambda_679C():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_679C)

    def lambda_67B4():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67B4)

    def lambda_67CC():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_67CC)

    def lambda_67DC():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_67DC)

    def lambda_67EC():
        OP_8F(0xFE, 0x4B0, 0xFA0, 0x532, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_67EC)

    def lambda_6807():
        OP_8F(0xFE, 0xFFFFFCE0, 0xFA0, 0x532, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6807)
    PlayEffect(0x6, 0x1, 0x18, -100, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x3, 0x19, 0, 500, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x5, 0x18, -100, 500, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x19, 0, 700, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)

    def lambda_691F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_691F)

    def lambda_6931():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_6931)
    OP_22(0x99, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x15,
        "#1504F#6PThat looks like...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x3, 0x18, -100, 500, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x19, 0, 700, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_6AC6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6AC6)

    def lambda_6AD8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_6AD8)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #134
        0x18,
        "Prince Olivert",
        "#1544F#5P...Mm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x19,
        "#572F#6P...Guh...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x18, 20)
    SetChrSubChip(0x18, 0)
    Sleep(150)
    SetChrChipByIndex(0x19, 22)
    SetChrSubChip(0x19, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #136
        0x18,
        "Prince Olivert",
        "#1543F#5PZin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x19,
        (
            "#073F#6PPrince Olivert? Now, this is a surprise.\x02\x03",

            "#573FDon't think this is a dream, at least...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0x18,
        "Prince Olivert",
        (
            "#1545F#5PIndeed, it is not.\x02\x03",

            "#1540FI would be overjoyed to share a sweet date\x01",
            "with Schera in my dreams. One with a fine\x01",
            "drinking companion...not so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x19,
        (
            "#071F#6PHaha! Yeah, this is real, all right.\x02\x03",

            "#070FStill, doesn't Schera count as a drinking\x01",
            "companion, too?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #140
        0x18,
        "Prince Olivert",
        (
            "#1544F#5PIn a way. It's fine to be drunk with the joy\x01",
            "of her company, but it is very much the\x01",
            "opposite to be drunk with alcohol involved.\x02\x03",

            "That's one of the most important lessons\x01",
            "I learned during my stay in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x19,
        (
            "#573F#6PHeh! Truer words have never been spoken.\x02\x03",

            "#070F...But all right. Enough playing around.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x18, 10)
    SetChrSubChip(0x18, 0)
    Sleep(100)
    SetChrChipByIndex(0x19, 11)
    SetChrSubChip(0x19, 0)
    OP_0D()
    Sleep(300)

    def lambda_6E8C():
        OP_6D(-1210, 4000, 510, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E8C)

    def lambda_6EA4():
        OP_8C(0x18, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6EA4)
    Sleep(100)
    OP_8C(0x19, 180, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #142
        0x19,
        (
            "#070F#11PYou guys mind filling us in on just what kind\x01",
            "of situation we've gotten ourselves into?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #143
        0x18,
        "Prince Olivert",
        (
            "#1541F#5PWe shall make with the embraces and tearful\x01",
            "greetings afterward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x13,
        "#274F#6PHonestly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x109,
        (
            "#1075F#6PYou two really are somethin' special.\x02\x03",

            "#1840FYou'd think you'd be a little shaken finding\x01",
            "yourselves in somewhere as unnatural as this \x01",
            "outta nowhere.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 720, 4000, -1550, 0)
    SetChrPos(0x10F, 350, 4000, -2930, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x11, 2750, 4000, -2390, 315)
    SetChrPos(0x12, 3080, 4000, -5090, 0)
    SetChrPos(0x13, 2140, 4000, -3370, 0)
    SetChrPos(0x14, 0, 4000, -4800, 0)
    SetChrPos(0x15, 1120, 4000, -4450, 0)
    SetChrPos(0x16, 3740, 4000, -4210, 315)
    SetChrPos(0x18, 1470, 4000, 670, 180)
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x19, 0, 4000, 620, 180)
    ClearChrFlags(0x19, 0x40)
    ClearChrFlags(0x19, 0x4)
    OP_6D(-20, 4000, -440, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(314000, 0)
    OP_6E(399, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #146
        0x19,
        "#074F#5PHmm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #147
        0x18,
        "Prince Olivert",
        "#1544F#11PThis is quite the pickle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x13,
        (
            "#272F#6PI appreciate that it may be hard to believe,\x01",
            "but that is the situation we find ourselves in\x01",
            "at this present time.\x02\x03",

            "#270FIf we're to try and find a way out, we'll need\x01",
            "you to accept that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #149
        0x18,
        "Prince Olivert",
        (
            "#1541F#11POh, Mueller. My sweet, rose-kissed muse, ever\x01",
            "pure and free of thorns. You misunderstand me.\x02\x03",

            "#1540FI have long accepted our current predicament as\x01",
            "reality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x13,
        "#273F#6PThen why do you look so deep in thought?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #151
        0x18,
        "Prince Olivert",
        (
            "#1540F#11PNeed you even ask?\x02\x03",

            "#1545FPerhaps my life's toughest decision lies ahead\x01",
            "of me.\x02\x03",

            "Before me, I find Joshua, Princess Klaudia,\x01",
            "Tita, and Josette. Then there's Julia and even\x01",
            "a new face: Ries.\x02\x03",

            "#1547FJust whom shall I gather into my arms like\x01",
            "a warm blanket and exchange sweet nothings\x01",
            "in celebration first?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #152
        0x13,
        "#274F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x11,
        "#067F#6PA-Ahaha..\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x16,
        "#1382F#6PHeehee... Only you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x14,
        (
            "#413F#6PUhh... Joshua?\x02\x03",

            "#212FYou were pulling my leg when you said this\x01",
            "guy was an Erebonian prince, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x15,
        "#1514F#6PHaha... Hard as it is to believe, he is.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #157
        0x18,
        "Prince Olivert",
        (
            "#1545F#11PPutting my deeply earnest dilemma aside\x01",
            "for the time being...\x02\x03",

            "#1540F...it sounds as though you've been making\x01",
            "some headway in unraveling the mysteries\x01",
            "behind this place.\x02\x03",

            "Naturally, I would be more than honored to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x19,
        (
            "#074F#5PBuuut first, you've got a few questions you\x01",
            "need to ask, right?\x02\x03",

            "#070FI know I sure do.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #159
        0x18,
        "Prince Olivert",
        (
            "#1541F#11PI should have known you would be thinking\x01",
            "along the same lines.\x02\x03",

            "#1540FYou're exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x109,
        "#1079F#6PFine by me. What do you want to ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x15,
        "#1502F#6PDo you think you've figured something out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x19,
        (
            "#074F#5PThat's what I want to find out.\x02\x03",

            "#072FFirst, I want to ask about that ghost you've\x01",
            "encountered in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x12,
        "#178F#6PAsk away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x16,
        (
            "#1162F#6PIf I remember correctly, the first time you met \x01",
            "her was on the balcony in Grancel Castle, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        (
            "#176F#6PIndeed, it was. She gave us the key that allowed\x01",
            "us to eventually find and rescue you.\x02\x03",

            "#178FThat was the first time she appeared to us as a\x01",
            "ghost, but I don't believe it was the first time she\x01",
            "directly communicated with you, was it, Father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x109,
        (
            "#1065F#5PDon't think so, anyway.\x02\x03",

            "#1060FWhen Ries and I first arrived here, we heard\x01",
            "a strange voice talking to us. We didn't have\x01",
            "a clue who it belong to at the time...\x02\x03",

            "...but I think that was probably her, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1446F#5PAs do I.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        (
            "#062F#6PSo at first, she existed here only as a voice,\x01",
            "but she's gradually started showing up with\x01",
            "a body, too?\x02\x03",

            "I know that's a weird way to put it, but if it's\x01",
            "true, it backs up what that man in black said\x01",
            "last time we saw him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x109,
        (
            "#1065F#5PYeah... He said the Lord of Phantasma had \x01",
            "stolen most of her power, right?\x02\x03",

            "#1063FHe kept referring to her as 'the hermit' and\x01",
            "'master of the hollow garden,' too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x19,
        (
            "#074F#5PPlus the inscription on that monument behind\x01",
            "us has 'The Hermit's Garden' written on it.\x02\x03",

            "#072FI think all of us here can connect the dots\x01",
            "just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x13,
        (
            "#277F#6PAgreed. It's reasonable to conclude that this\x01",
            "very garden is connected to her in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x16,
        "#1164F#6PThat's true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x14,
        (
            "#210F#6PMakes sense to me.\x02\x03",

            "It also explains why this place is kinda comfy\x01",
            "compared to the other weird, fiend-infested\x01",
            "places in Phantasma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x109,
        (
            "#1075F#5PHmm... Feels like we're getting closer to the\x01",
            "truth with every new revelation.\x02\x03",

            "#1060FBy the sounds of it, she's been in Phantasma\x01",
            "for a while now. Possibly since the beginning.\x02\x03",

            "But then she had her power stolen by the Lord\x01",
            "of Phantasma and ended up without a body.\x02\x03",

            "Since then, she's been trying to help us to the\x01",
            "best of her abilities and guide us forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x15,
        (
            "#1513F#6PIf we assume all of that to be true, maybe\x01",
            "the monuments scattered throughout are\x01",
            "connected to her somehow, too.\x02\x03",

            "#1500FThey seem to exist for that same purpose:\x01",
            "guiding us forward.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #176
        0x18,
        "Prince Olivert",
        (
            "#1545F#11PI think there's one more thing in our possession\x01",
            "that's connected to her as well.\x02\x03",

            "#1540FThat cube, Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x109,
        "#1079F#6PYou think so?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #178
        0x18,
        "Prince Olivert",
        (
            "#1540F#11PUnfortunately, your guess is as good as mine\x01",
            "on exactly what that cube is.\x02\x03",

            "That being said, I think the odds of it being\x01",
            "connected to her somehow are as high as\x01",
            "everything else on the list so far.\x02\x03",

            "#1541FWell? What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x109,
        (
            "#1075F#6P...Honestly, I'm impressed.\x02\x03",

            "#1840FYou've done a remarkable job of making\x01",
            "sense of the situation when you've only\x01",
            "just arrived.\x02\x03",

            "Still, if we assume all that to be true, then\x01",
            "there's something else we should be doing\x01",
            "as we keep moving forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x16,
        (
            "#1383F#6PHelping to restore her power, I assume?\x02\x03",

            "#1160FThat way, we should be able to ask her what\x01",
            "else she knows about the land we're in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x109,
        (
            "#1065F#5PGot it in one.\x02\x03",

            "#1063FI get this impression that if we don't, we won't\x01",
            "stand a chance against those two--we'll find\x01",
            "ourselves up against a wall at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x12,
        "#178F#6PYou may well be right...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #183
        0x18,
        "Prince Olivert",
        (
            "#1541F#11PWell, leaving her aside for the time being...\x02\x03",

            "#1540F...I do have one final thing I'd like to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x109,
        "#1064F#6PHuh? What else is there to cover?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #185
        0x18,
        "Prince Olivert",
        (
            "#1545F#11PIt concerns that Lord of Phantasma you kept\x01",
            "mentioning, actually.\x02\x03",

            "#1540FPut simply, you wouldn't happen to have any\x01",
            "idea as to who they are, would you, Kevin?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #186
        0x10F,
        "#1445F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x109,
        "#1840F#6P...Why me?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #188
        0x18,
        "Prince Olivert",
        (
            "#1540F#11PWell, from my perspective, they're awfully fixated\x01",
            "on you.\x02\x03",

            "#1544FThey seemed to know about Ries' deceased sister\x01",
            "as well... Then there's the fact they're even able\x01",
            "to summon devils from the church's texts.\x02\x03",

            "It all seems to be pointing to you two--and you in\x01",
            "particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x109,
        (
            "#1065F#6PHmm... I can see why you'd ask, I guess.\x02\x03",

            "#1840FUnfortunately for you, though, I got nothin'.\x02\x03",

            "If anything, I'd say they seem to be an enemy\x01",
            "of the Gralsritter as a whole rather than just\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10F,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0x18,
        "Prince Olivert",
        (
            "#1542F#11PHmm... I suppose that's possible. I wouldn't be\x01",
            "surprised if an organization like that had more\x01",
            "than their fair share of enemies.\x02\x03",

            "#1545FNo offense, of course. I have plenty of enemies,\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x13,
        (
            "#272F#6PTry not to sound like it's something worth\x01",
            "boasting about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x15,
        (
            "#1503F#6PAnyway, even if we've connected some dots,\x01",
            "we'll have to save the mystery behind who our\x01",
            "enemies are for another day.\x02\x03",

            "#1502FMaybe we can get more information out of\x01",
            "them the next time we see them, but until\x01",
            "then, we don't have enough to work with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x109,
        (
            "#1075F#5PRight. Next time one of them shows up,\x01",
            "we'll have to see what we can force out\x01",
            "of them.\x02\x03",

            "#1078FSo, that about wrap things up for now?\x01",
            "If so, we should probably get ready to\x01",
            "head out again.\x02\x03",

            "We're on plane number four, and if the\x01",
            "previous planes are anything to go by,\x01",
            "it's gonna be tough.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #195
        0x10F,
        "#1446F#6P...Kevin.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8C96():
        OP_6D(-70, 4000, -1410, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C96)

    def lambda_8CAE():
        OP_8C(0x109, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8CAE)
    Sleep(100)

    def lambda_8CC1():

        label("loc_8CC1")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8CC1")

    QueueWorkItem2(0x11, 3, lambda_8CC1)

    def lambda_8CD2():

        label("loc_8CD2")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8CD2")

    QueueWorkItem2(0x12, 3, lambda_8CD2)
    Sleep(100)

    def lambda_8CE8():

        label("loc_8CE8")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8CE8")

    QueueWorkItem2(0x13, 3, lambda_8CE8)

    def lambda_8CF9():

        label("loc_8CF9")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8CF9")

    QueueWorkItem2(0x16, 3, lambda_8CF9)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #196
        0x109,
        (
            "#1079F#11PHmm? What's up?\x02\x03",

            "Did you have something else you wanted to add?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10F,
        (
            "#1446F#6PNo.\x02\x03",

            "#1805FIt's just that I'm not feeling very well,\x01",
            "so I'm going to sit the next plane out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x109,
        "#1064F#11PWha...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(500)

    ChrTalk(    #199
        0x10F,
        (
            "#1806F#5PI'm sorry for the trouble, everyone...but\x01",
            "please look out for him on my behalf.\x02\x03",

            "He shouldn't cause you too much trouble,\x01",
            "but as I'm sure you know, he can be a little\x01",
            "careless at times.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8EB9():
        OP_6D(40, 4000, -2960, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8EB9)

    def lambda_8ED1():
        OP_6B(2400, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8ED1)
    OP_43(0x10F, 0x0, 0x2, 0x8)

    def lambda_8EE8():

        label("loc_8EE8")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8EE8")

    QueueWorkItem2(0x109, 3, lambda_8EE8)

    def lambda_8EF9():

        label("loc_8EF9")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8EF9")

    QueueWorkItem2(0x14, 3, lambda_8EF9)

    def lambda_8F0A():

        label("loc_8F0A")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8F0A")

    QueueWorkItem2(0x15, 3, lambda_8F0A)

    def lambda_8F1B():

        label("loc_8F1B")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8F1B")

    QueueWorkItem2(0x18, 3, lambda_8F1B)

    def lambda_8F2C():

        label("loc_8F2C")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_8F2C")

    QueueWorkItem2(0x19, 3, lambda_8F2C)
    Sleep(1500)

    ChrTalk(    #200 op#A
        0x11,
        "#065F#11P#25AR-Ries?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #201 op#A
        0x14,
        "#213F#11P#12AW-Wait a sec!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x109, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x19, 0x3)
    Fade(500)
    OP_6D(270, 4000, -1010, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(314000, 0)
    OP_6E(399, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #202
        0x109,
        "#1079F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x19,
        "#072F#11PAre you not gonna go after her?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #204
        0x109,
        (
            "#1064F#6PI... Umm...\x02\x03",

            "#1067F...Sorry. I'll be back in a minute.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x109, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_6014 end

    def Function_7_90C3(): pass

    label("Function_7_90C3")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFF0EC, 0x1388, 0x0)
    OP_8E(0xFE, 0xC8, 0x3E8, 0xFFFFA77C, 0x1388, 0x0)
    Return()

    # Function_7_90C3 end

    def Function_8_90F3(): pass

    label("Function_8_90F3")

    OP_8C(0xFE, 270, 400)
    Sleep(100)
    OP_8E(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFF0EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x1004, 0xFFFFC964, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_90F3 end

    def Function_9_912D(): pass

    label("Function_9_912D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_912D end

    def Function_10_91FA(): pass

    label("Function_10_91FA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x260083, 0x260088, 0x13)
    OP_D2(0x260285, 0x26028A, 0x14)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -60, 4000, -1440, 0)
    SetChrPos(0x102, 650, 4000, -2750, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x11, -950, 4000, -3010, 0)
    SetChrPos(0x12, -1390, 4000, -5900, 0)
    SetChrPos(0x13, 100, 4000, -6000, 0)
    SetChrPos(0x14, -2140, 4000, -4920, 0)
    SetChrPos(0x16, -740, 4000, -4410, 0)
    SetChrPos(0x18, 500, 4000, -4520, 0)
    SetChrPos(0x19, 1410, 4000, -5260, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1220, 4000, -590, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_93A5():
        OP_6D(1760, 4000, 3840, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_93A5)

    def lambda_93BD():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93BD)

    def lambda_93D5():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93D5)

    def lambda_93E5():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_93E5)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 20)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1A, 0x80)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x2)
    ClearChrFlags(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 19)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x1A, 100, 5400, 0, 0)
    PlayEffect(0x1, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_94FC():
        OP_8F(0xFE, 0x64, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_94FC)
    WaitChrThread(0x1A, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1A, 0, 6000, 1000, 0)

    def lambda_957E():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_957E)

    def lambda_9596():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9596)

    def lambda_95AE():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_95AE)

    def lambda_95BE():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_95BE)

    def lambda_95CE():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_95CE)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_95F8():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_95F8)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1A, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x146)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2D8, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(3000)
    OP_6D(1090, 5000, 1260, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(33000, 0)
    OP_6E(365, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)
    SetChrPos(0x109, 100, 4000, -1290, 0)
    SetChrPos(0x1A, -390, 8000, 2150, 180)
    SetChrSubChip(0x1A, 0)
    PlayEffect(0x6, 0x0, 0x1A, -500, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_9855():
        OP_6D(1730, 4000, 2029, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9855)

    def lambda_986D():
        OP_67(0, 4350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_986D)

    def lambda_9885():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9885)

    def lambda_9895():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9895)

    def lambda_98A5():
        OP_8F(0xFE, 0xFFFFFE7A, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_98A5)
    WaitChrThread(0x1A, 0x0)
    SetChrSubChip(0x1A, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1A, -500, 700, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_990E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_990E)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Sleep(1000)

    ChrTalk(    #205
        0x109,
        "#1079F#6PH-Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1504F#6PIs she...sleeping?\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x1A, -500, 700, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_9A8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_9A8E)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1A, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #207
        0x1A,
        (
            "#1316F#5P#40WZzz... Mmm...\x02\x03",

            "#817FCuteness is...justice...\x02\x03",

            "Fortune favors the cute...\x02\x03",

            "Keep your friends close and...your plushies \x01",
            "closer...\x02\x03",

            "#1311FHeehee... Smart words from smart people...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #208
        0x109,
        (
            "#1068F#6PI don't think anyone else in history has ever\x01",
            "said any of those things. Especially that last\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        "#067F#6PShe seems so happy, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#1514F#6PHaha... Yeah, I'm not sure I can bring myself\x01",
            "to wake her up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x18,
        (
            "#1541F#5PIn that case, I have a plan of my own.\x02\x03",

            "#1547FI shall sleep alongside her, and together we shall\x01",
            "reach the pearled gates of Elysium and cross into\x01",
            "the paradise within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x13,
        (
            "#277F#6PIf you're up for a nap, that can be arranged.\x01",
            "I have a few tricks that could knock you out\x01",
            "in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x18,
        "#1544F#5PI'msorrypleasedon'thurtme.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x16,
        "#1165F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x19,
        "#071F#11PHey, you tried!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1A,
        "#1316F#5PMm...\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x0, 0x2, 0x3E8)
    OP_99(0x1A, 0x2, 0x0, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0x0, 0x3, 0x3E8)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x12,
        "#170F#5PSeems she's finally woken up.\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x3, 0x7, 0x3E8)
    Sleep(500)

    ChrTalk(    #218
        0x1A,
        (
            "#813F#5P#40W...Huh?\x01",
            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        "#1500F#6PIt's good to see you again, Anelace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x11,
        "#560F#6PUmm... Good morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x109,
        (
            "#1066F#6PHave a nice dream? Sure sounded like\x01",
            "you were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x1A,
        "#814F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x7, 0x9, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0x9, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0xD, 0x13, 0x3E8)
    OP_99(0x1A, 0x10, 0x13, 0x3E8)
    Sleep(300)

    ChrTalk(    #223
        0x1A,
        (
            "#1314F#5P#40WHmm... Tita, Joshua, and Kloe are going to be\x01",
            "the pride of my collection...\x02\x03",

            "Buuut Julia and that girl over there are pretty\x01",
            "cute, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x14,
        "#213F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x16,
        "#1164F#6PWhat're you talking about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x1A,
        (
            "#814F#5P#40WOh, but Zin's like a big fluffy bear, so he's\x01",
            "actually kinda nice...\x02\x03",

            "And Kevin's hair kinda reminds me of a sea\x01",
            "urchin, and that's not so bad, either...\x02\x03",

            "#811FHeeheehee... I dunno who bought me all these\x01",
            "new plushies, but they're the best.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #227
        0x102,
        "#1512F#6P...She thinks we're all life-sized stuffed toys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x109,
        "#1068F#6PMan, how drowsy do you have to be?\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -140, 4000, -2170, 0)
    SetChrPos(0x102, 720, 4000, -3150, 0)
    SetChrPos(0x11, -1420, 4000, -3440, 0)
    SetChrPos(0x12, -1800, 4000, -5800, 0)
    SetChrPos(0x13, -400, 4000, -5850, 0)
    SetChrPos(0x14, -2500, 4000, -4800, 0)
    SetChrPos(0x16, -710, 4000, -4290, 0)
    SetChrPos(0x18, 500, 4000, -4400, 0)
    SetChrPos(0x19, 950, 4000, -5300, 0)
    SetChrPos(0x1A, 90, 4000, -340, 180)
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x1A, 0x2)
    SetChrFlags(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    OP_6D(1230, 4000, -1300, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #229
        0x1A,
        (
            "#1316F#5PAww... There was me thinking I'd gotten\x01",
            "a bunch of amazing new plushies to add\x01",
            "to my collection.\x02\x03",

            "Way to crush a girl's dreams, guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x102,
        "#1508F#6PWell, sorry for being a human being...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x109,
        (
            "#1068F#6PI can't believe that's your first reaction\x01",
            "to everything you've just been told...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x1A,
        (
            "#1315F#5PAhaha. Sorry! I'll hop into serious mode now.\x02\x03",

            "#812FI'm still having a heck of a time processing the\x01",
            "situation, but I DO know you're not lying.\x02\x03",

            "#815FBesides, the proof that this is all real is right\x01",
            "in front of my eyes. Only the real Tita can be\x01",
            "THAT irresistibly cute!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #233
        0x11,
        "#067F#6PHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x109,
        (
            "#1075F#6PWell, just as long as you get it.\x02\x03",

            "#1060FSo what are you going to do? Would you be\x01",
            "up for helping us investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x1A,
        (
            "#816F#5PPut me in, coach!\x02\x03",

            "I wouldn't be much of a bracer if I wasn't\x01",
            "willing to do anything in the face of a crisis\x01",
            "like this!\x02\x03",

            "#817FEspecially if it's true something's happened\x01",
            "to Le Locle.\x02\x03",

            "#812FThere might be other bracers there who've\x01",
            "ended up in the same situation as me, and\x01",
            "no way I'm turning my back on them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x12,
        "#176F#6PThat's certainly a possibility...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x11,
        "#065F#6PO-Other bracers? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#1503F#5PThat's a good point... We know quite a few of\x01",
            "them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x109,
        (
            "#1065F#5PWell, we've overcome one ordeal, but that still\x01",
            "means we have two left on our plates.\x02\x03",

            "#1060FAnd you know the drill--now that we've done\x01",
            "the first, let's go back to the fourth plane and\x01",
            "see what's changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#1500F#6PRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x18,
        "#1541F#6PLet the fun begin anew.\x02",
    )

    CloseMessageWindow()

    def lambda_AB46():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AB46)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2905)
    OP_28(0x33, 0x4, 0x4)
    OP_28(0x33, 0x4, 0x8)
    OP_3F(0x35A, 1)
    OP_3F(0x32C, 1)
    OP_3E(0x32D, 1)
    OP_DB(0x0, 0x9)
    OP_A2(0x25CF)
    Call(6, 18)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_91FA end

    def Function_11_ACF8(): pass

    label("Function_11_ACF8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x270033, 0x270038, 0x13)
    OP_D2(0x270034, 0x270039, 0x14)
    OP_D2(0x260285, 0x26028A, 0x15)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -320, 4000, -2790, 0)
    SetChrPos(0x102, -1330, 4000, -3360, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x11, 1030, 4000, -3520, 0)
    SetChrPos(0x12, 1540, 4000, -6410, 0)
    SetChrPos(0x13, 80, 4000, -6280, 0)
    SetChrPos(0x14, 2320, 4000, -5750, 0)
    SetChrPos(0x16, 730, 4000, -4710, 0)
    SetChrPos(0x18, -570, 4000, -4740, 0)
    SetChrPos(0x19, -1600, 4000, -5240, 0)
    SetChrPos(0x1A, 2400, 4000, -4510, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_AEC3():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEC3)

    def lambda_AEDB():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEDB)

    def lambda_AEF3():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AEF3)

    def lambda_AF03():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_AF03)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1B, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x1)
    SetChrChipByIndex(0x1B, 19)
    SetChrSubChip(0x1B, 0)
    SetChrPos(0x1B, 0, 5200, 100, 0)
    PlayEffect(0x1, 0x0, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_B015():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_B015)
    WaitChrThread(0x1B, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1B, 0, 6000, 1000, 0)

    def lambda_B097():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B097)

    def lambda_B0AF():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B0AF)

    def lambda_B0C7():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B0C7)

    def lambda_B0D7():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0D7)

    def lambda_B0E7():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_B0E7)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_B111():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B111)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1B, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x146)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2D8, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(3000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x109, -220, 4000, -1910, 0)
    SetChrPos(0x11, 800, 4000, -3520, 0)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 390, 3700, 1800, 180)
    SetChrPos(0x1B, 390, 8000, 2150, 180)
    SetChrSubChip(0x1B, 0)
    PlayEffect(0x6, 0x0, 0x1B, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_B3A0():
        OP_6D(-1510, 4000, 800, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B3A0)

    def lambda_B3B8():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B3B8)

    def lambda_B3D0():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B3D0)

    def lambda_B3E0():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B3E0)

    def lambda_B3F0():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_B3F0)
    WaitChrThread(0x1B, 0x0)
    SetChrSubChip(0x1B, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1B, 300, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_B459():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_B459)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #242
        0x109,
        "#1079F#6P...H-Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        "#1502F#6PThat's not Schera...is it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1B, 300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_B4FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_B4FC)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1B, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #244
        0x1B,
        "#1525F#11P...H-Huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #245
        0x11,
        "#064FOh#6P!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        "#1504F#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x16,
        "#1164F#6POh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x18,
        "#1543F#6PMy goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x19,
        "#070F#6PShe cut her hair, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x1A,
        (
            "#811F#6PYep. About a month or so ago.\x02\x03",

            "#1310FShe got herself some new duds\x01",
            "to match, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #251
        0x1B,
        (
            "#1532F#11PUgh... This isn't like me at all...\x02\x03",

            "I haven't had anywhere near enough to drink\x01",
            "to start feeling this out of whack...\x02\x03",

            "#1526F...No! There's no stopping me now!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x1B, 20)
    SetChrSubChip(0x1B, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #252
        0x1B,
        (
            "#1524F#3S#11PPour me another, Aina! Tonight, we're going\x01",
            "to settle this once and for a--\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #253
        0x1B,
        (
            "#1523F#11P...Dwah?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        "#1513F#6PNice to see you, Schera.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x1B, 13)
    SetChrSubChip(0x1B, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #255
        0x1B,
        (
            "#1523F#11PJoshua?!\x02\x03",

            "#1521FHow long have you been back for? What happened\x01",
            "to Estelle?\x02\x03",

            "#1536FAnd is it just me, or did you put on some muscle\x01",
            "while you were away? You look stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x102,
        "#1514F#6PHaha... Thanks. I'm happy to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x18,
        (
            "#1545F#6PBe as it may, I can't believe you still haven't\x01",
            "commented on my presence.\x02\x03",

            "#1540FHow could you disregard your dear Olivier\x01",
            "Lenheim, your loyal servant, and the man\x01",
            "who forever holds the key to your heart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x1B,
        (
            "#1523F#11PO-Olivier?!\x02\x03",

            "Wait... You're not the only familiar faces here...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x1B, 90, 400)
    Sleep(500)
    OP_8C(0x1B, 0, 400)
    Sleep(500)
    OP_8C(0x1B, 270, 400)
    Sleep(500)

    ChrTalk(    #259
        0x1B,
        (
            "#1525F#5PTh-This whole place is kind of...bizarre, too...\x02\x03",

            "#1524FCan someone explain what's going on here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x1A,
        "#819F#6PWe will, we will. So calm down, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x16,
        (
            "#1165F#6PHeehee... I can hardly blame you for\x01",
            "being surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x14,
        (
            "#210F#6PYeah. Your reaction's par for the course\x01",
            "for this place.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_63(0x1B)
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x102, -570, 4000, -2720, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x11, 2320, 4000, -3080, 315)
    SetChrPos(0x12, 2370, 4000, -5810, 0)
    SetChrPos(0x13, 910, 4000, -5690, 0)
    SetChrPos(0x14, 3660, 4000, -5200, 315)
    SetChrPos(0x16, 1810, 4000, -4220, 0)
    SetChrPos(0x18, 220, 4000, -4110, 0)
    SetChrPos(0x19, -770, 4000, -4950, 0)
    SetChrPos(0x1A, 3970, 4000, -3980, 315)
    SetChrPos(0x1B, 290, 4000, -190, 180)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1B, 13)
    SetChrSubChip(0x1B, 0)
    SetChrFlags(0x10, 0x80)
    OP_6D(-430, 4000, -900, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #263
        0x1B,
        (
            "#1526F#11P*cough* Okay, I THINK I get what's going on\x01",
            "now.\x02\x03",

            "#1534FStill, under ordinary circumstances, I'd have a\x01",
            "pretty hard time believing all of what you said\x01",
            "was even possible.\x02\x03",

            "It's easier to chalk this up as just an alcohol-\x01",
            "induced dream or another of Luci's illusions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x109,
        "#1840F#6PHaha... No doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x18,
        (
            "#1546FOh, woe is me!\x02\x03",

            "#1544FHow could you look upon my fair countenance\x01",
            "and beautiful locks and not believe that I am\x01",
            "the one, the ONLY true Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1B,
        (
            "#1525F#11PI said, 'Under ordinary circumstances,' Olivier.\x01",
            "There's no need for the dramatics.\x02\x03",

            "#1527FFirst, what would be the point of showing me\x01",
            "an illusion this bizarre to begin with?\x02\x03",

            "As for the dream explanation...there's a bit too\x01",
            "much internal consistency here for me to lean\x01",
            "on that theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x19,
        "#071F#6PHaha. True enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x109,
        (
            "#1075F#6PThanks for believing us.\x02\x03",

            "#1060FSo I take it you'll be up for helping us, then?\x01",
            "We could sure use you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x1B,
        (
            "#1520F#11PI'd be happy to.\x02\x03",

            "#1526FWhen I think about how Estelle's mostly likely\x01",
            "been dragged into this place, too, how could\x01",
            "I think to say no?\x02\x03",

            "#1536FI wouldn't be a good big sister if I didn't look\x01",
            "out for my little sis, now, would I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        "#1501F#6PThanks, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x18,
        "#1541FYou are a true model of a woman.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x109,
        (
            "#1077F#6PCheers. We appreciate it.\x02\x03",

            "#1078FAnyway, we've given you a rough outline of\x01",
            "the situation we're in.\x02\x03",

            "Currently, we're in the middle of exploring\x01",
            "what's apparently called the fourth plane,\x01",
            "so that's where we'll be resuming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x1B,
        (
            "#1526F#11PAll right.\x02\x03",

            "I've used the facilities at Le Locle before as a\x01",
            "trainee back in the day.\x02\x03",

            "#1522FSince you've found both me and Anelace there\x01",
            "so far, perhaps the other sealing stones you find\x01",
            "there will contain people who trained there, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x19,
        "#072F#6PSounds plausible enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1A,
        (
            "#1317F#6PThat means the chance we'll find Estelle\x01",
            "there is high...\x02\x03",

            "Or, I dunno. Maybe we'll find Kurt, Grant,\x01",
            "or Carna?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x1B,
        (
            "#1526F#11PIt's not impossible.\x02\x03",

            "#1520FThey've certainly been to Le Locle, but\x01",
            "they went more as instructors.\x02\x03",

            "I don't think they've ever been purely as\x01",
            "trainees the way you, Estelle, and I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1A,
        "#814F#6POh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x11,
        (
            "#065F#6PHey, Schera...?\x02\x03",

            "Has, erm... Do you know if Agate has ever\x01",
            "trained there before?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_C653():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_C653)
    Sleep(50)

    def lambda_C666():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C666)
    Sleep(50)

    def lambda_C679():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C679)
    Sleep(50)

    def lambda_C68C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_C68C)
    Sleep(50)

    def lambda_C69F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_C69F)
    Sleep(400)

    ChrTalk(    #279
        0x1B,
        (
            "#1526F#5PNow you mention it, yes. He has.\x02\x03",

            "#1534FCassius supposedly tricked him into going,\x01",
            "and he was...not a fan of the experience.\x02\x03",

            "That was about four years ago, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x11,
        (
            "#063F#6PO-Oh...\x02\x03",

            "#562FSo that means both him and Estelle might be \x01",
            "trapped there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        "#1503F#5PIt's possible, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x16,
        (
            "#1383F#6P...They're both fine.\x02\x01",

            "#1168FI'm certain of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x12,
        (
            "#170F#6PAt any rate, we now have only one of the\x01",
            "three ordeals remaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x13,
        (
            "#278F#6PIndeed.\x02\x03",

            "#277FSo we'll find who else is trapped inside the\x01",
            "training ground soon enough--and then all\x01",
            "that remains is for us to rescue them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x109,
        "#1060F#5PYup. So as soon as we're ready, let's move.\x02",
    )

    CloseMessageWindow()

    def lambda_C944():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C944)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x290A)
    OP_28(0x34, 0x4, 0x4)
    OP_28(0x34, 0x4, 0x8)
    OP_3F(0x35B, 1)
    OP_3F(0x32D, 1)
    OP_3E(0x32E, 1)
    OP_DB(0x0, 0x2)
    OP_A2(0x25C8)
    Call(6, 12)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_ACF8 end

    def Function_12_CAFB(): pass

    label("Function_12_CAFB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x70054, 0x7005C, 0x13)
    OP_D2(0x70055, 0x7005D, 0x14)
    OP_D2(0x60119, 0x6011E, 0x15)
    OP_D2(0x260285, 0x26028A, 0x16)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -90, 4000, -2980, 0)
    SetChrPos(0x102, 1080, 4000, -3580, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x11, -1450, 4000, -4380, 0)
    SetChrPos(0x12, -1100, 4000, -6420, 0)
    SetChrPos(0x13, 250, 4000, -6490, 0)
    SetChrPos(0x14, -2040, 4000, -5910, 0)
    SetChrPos(0x16, -410, 4000, -4920, 0)
    SetChrPos(0x18, 820, 4000, -5000, 0)
    SetChrPos(0x19, 2100, 4000, -6330, 0)
    SetChrPos(0x1A, 2270, 4000, -4300, 0)
    SetChrPos(0x1B, 1650, 4000, -5520, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1220, 4000, -590, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_CCE6():
        OP_6D(1760, 4000, 3840, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CCE6)

    def lambda_CCFE():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCFE)

    def lambda_CD16():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CD16)

    def lambda_CD26():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_CD26)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 22)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1C, 0x80)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x1)
    SetChrChipByIndex(0x1C, 19)
    SetChrSubChip(0x1C, 0)
    SetChrPos(0x1C, 100, 5400, 0, 0)
    PlayEffect(0x1, 0x0, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_CE38():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_CE38)
    WaitChrThread(0x1C, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1C, 0, 6000, 1000, 0)

    def lambda_CEBA():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CEBA)

    def lambda_CED2():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CED2)

    def lambda_CEEA():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CEEA)

    def lambda_CEFA():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEFA)

    def lambda_CF0A():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_CF0A)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_CF34():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CF34)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1C, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_CAFB end

    def Function_13_D01E(): pass

    label("Function_13_D01E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x70054, 0x7005C, 0x13)
    OP_D2(0x70055, 0x7005D, 0x14)
    OP_D2(0x70061, 0x70069, 0x15)
    OP_D2(0x60119, 0x6011E, 0x16)
    OP_D2(0x2602CA, 0x2602CF, 0x17)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x11, -400, 4000, -1900, 0)
    SetChrPos(0x109, 190, 4000, -3230, 0)
    SetChrPos(0x102, -1570, 4000, -3620, 0)
    SetChrPos(0x12, -2190, 4000, -6100, 0)
    SetChrPos(0x13, -720, 4000, -6410, 0)
    SetChrPos(0x14, -2800, 4000, -5090, 0)
    SetChrPos(0x16, -1180, 4000, -4830, 0)
    SetChrPos(0x18, 180, 4000, -4830, 0)
    SetChrPos(0x19, 1550, 4000, -6200, 0)
    SetChrPos(0x1A, 1540, 4000, -3560, 0)
    SetChrPos(0x1B, 1250, 4000, -5170, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1090, 5000, 1260, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x1C, 0x80)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x1)
    SetChrPos(0x1C, -390, 8000, 2150, 180)
    SetChrChipByIndex(0x1C, 19)
    SetChrSubChip(0x1C, 0)
    PlayEffect(0x3, 0x0, 0x1C, -400, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -390, 3700, 1900, 180)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_D25E():
        OP_6D(1730, 4000, 2029, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D25E)

    def lambda_D276():
        OP_67(300, 4350, -10300, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D276)

    def lambda_D28E():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D28E)

    def lambda_D29E():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_D29E)

    def lambda_D2AE():
        OP_8F(0xFE, 0xFFFFFE7A, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D2AE)
    WaitChrThread(0x1C, 0x0)
    SetChrSubChip(0x1C, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x3, 0x1, 0x1C, -400, 500, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_D317():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D317)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #286
        0x11,
        "#560F#6PYay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x102,
        "#1501F#6PHaha. Looks like you got your wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x109,
        (
            "#1071F#6PYou wouldn't find hair that red on\x01",
            "anyone else.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1C, -400, 500, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_D3FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D3FB)
    OP_82(0x2, 0x2)
    WaitChrThread(0x15, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #289
        0x1C,
        "#552F#5PUgh... The hell's going on?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x1C, 20)
    SetChrSubChip(0x1C, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #290
        0x1C,
        "#054F#3S#5PHey, Dan! What just happened?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #291
        0x1C,
        "#055F#5P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x11,
        "#560F#6PA-Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x1C,
        (
            "#052F#5PWhat're you doing here, Tita? I thought you were\x01",
            "busy fixing up dinner.\x02\x03",

            "#055FWait a sec...\x02\x03",

            "Where IS Dan, anyway? I thought I just got off the \x01",
            "airliner and bumped into him...but now you're here\x01",
            "and he's not... What's going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x11,
        "#562F#6P...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 21)

    def lambda_D5F7():
        OP_6D(1730, 4000, 3030, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D5F7)

    def lambda_D60F():
        OP_8E(0xFE, 0xFFFFFF74, 0xFA0, 0x640, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D60F)
    Sleep(500)
    Fade(500)
    OP_6D(770, 4000, 3030, 0)
    OP_67(0, 3550, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(36000, 0)
    OP_6E(299, 0)
    WaitChrThread(0x11, 0x0)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_22(0x20C, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #295
        0x1C,
        "#055F#5PH-Hey! Hurry up and fill me in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x11,
        (
            "#562F#12PI'm so happy you're okay...\x02\x03",

            "I'm so, so happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x1C,
        (
            "#551F#5POf course I'm okay... We only just saw each\x01",
            "other.\x02\x03",

            "#555FSince shortstuff here's started turnin' on the\x01",
            "waterworks, you up for filling me in on what's\x01",
            "going on instead, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #298
        0x1C,
        (
            "#052F#5P...Wait! Hold up! I didn't even know you were\x01",
            "back in Liberl!\x02\x03",

            "#055FAnd why's the priest here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D854():
        OP_6D(770, 4000, 1580, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D854)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #299
        0x102,
        "#1514F#6PHaha... It's a long story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x109,
        "#1840F#6PA REALLY long story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x1B,
        (
            "#1536F#8PJust in case you hadn't noticed, the rest\x01",
            "of us are here, too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x19,
        "#071F#8PGood to see you again, my friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x16,
        "#1168F#8PHeehee. It certainly is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x1A,
        (
            "#819F#8PI still wish we could trade places, though.\x01",
            "What I wouldn't give for Tita to be all over\x01",
            "me like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x18,
        (
            "#1541F#8PHe's truly the most fortunate man on\x01",
            "the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x1C,
        (
            "#055F#5PW-Will you shut your traps? There're some\x01",
            "really big misunderstandings going on here,\x01",
            "and I don't like it one bit!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)

    def lambda_DABB():
        OP_6D(770, 4000, 580, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DABB)

    def lambda_DAD3():
        OP_8F(0xFE, 0xFFFFFF88, 0xFA0, 0x32A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_DAD3)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1C, 14)
    SetChrSubChip(0x1C, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #307
        0x11,
        (
            "#067F#12PHeehee. I'm sorry, Agate. I was just so\x01",
            "happy that I couldn't help myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #308
        0x11,
        (
            "#061F#5PNow all we need to do is save Estelle,\x01",
            "and the whole group's back together\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x1C,
        (
            "#052F#5PHuh? Estelle?\x02\x03",

            "#055FSeriously, how many damn times do I gotta\x01",
            "ask before one of you coughs up an\x01",
            "explanation?\x02\x03",

            "This isn't another one of Erika's murderous\x01",
            "traps, is it?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #310
        0x109,
        (
            "#1068F#6PShe must REALLY have it in for you\x01",
            "if that's your first guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x102,
        (
            "#1514F#6PIt sounds like quite a lot's happened\x01",
            "since your parents came back, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x11,
        "#067F#5PYou could say that...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 150, 4000, -2370, 0)
    SetChrPos(0x102, -1230, 4000, -3650, 0)
    SetChrPos(0x11, 920, 4000, -3150, 0)
    SetChrPos(0x16, -900, 4000, -4520, 0)
    SetChrPos(0x18, 450, 4000, -4600, 0)
    SetChrPos(0x16, -950, 4000, -4770, 0)
    SetChrPos(0x14, -2390, 4000, -5120, 0)
    SetChrPos(0x13, -240, 4000, -6160, 0)
    SetChrPos(0x12, -1670, 4000, -6190, 0)
    SetChrPos(0x19, 1300, 4000, -6200, 0)
    SetChrPos(0x1A, 2000, 4000, -3500, 0)
    SetChrPos(0x1B, 1470, 4000, -5000, 0)
    SetChrPos(0x1C, 190, 4000, -340, 180)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1C, 14)
    SetChrSubChip(0x1C, 0)
    SetChrFlags(0x10, 0x80)
    OP_6D(1500, 4000, -1600, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #313
        0x1C,
        (
            "#555F#5PHmph. All right. Got it.\x02\x03",

            "I'll be honest: this whole thing still doesn't\x01",
            "feel quite real, but I can't see anything you\x01",
            "say changin' that.\x02\x03",

            "So I'm in. Let's get to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        "#1504F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x109,
        (
            "#1840F#6PHaha. That was quick.\x02\x03",

            "You sure you don't want to ask anything? We'll \x01",
            "try and answer as best we can if you've got any \x01",
            "burning questions to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x1C,
        (
            "#053F#5PNah. I've got a good idea of what the situation\x01",
            "is from your last explanation.\x02\x03",

            "As for the rest? I figure it's easier to just see\x01",
            "things for myself. Anything I need after that,\x01",
            "I'll ask someone.\x02\x03",

            "#556F'Sides, it just doesn't feel right having all\x01",
            "these people gathered and no Estelle.\x02\x03",

            "So let's go find her and put that right, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x11,
        "#560F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x102,
        "#1505F#6PThanks for helping us out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x1C,
        (
            "#551F#5PWhat're you thanking me for?\x02\x03",

            "Lookin' after younger bracers is part of the\x01",
            "job. That goes for you, too.\x02\x03",

            "#051FHow's it been for you these days, anyway?\x02\x03",

            "Feel like you've gotten any stronger through\x01",
            "that journey of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x102,
        (
            "#1513F#6PI'd like to think so.\x02\x03",

            "#1501FIf you ask me, Estelle's changed more than\x01",
            "I have, though. She's shaped up to be a real\x01",
            "reliable bracer these days.\x02\x03",

            "Whatever guild we go to, they seem to end\x01",
            "up needing her for this and that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x1C,
        "#051F#5PNo shit? Taking after her old man, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1B,
        (
            "#1536F#12PHaha. Still...\x02\x03",

            "...I'm amazed how quickly you accepted that\x01",
            "this was reality and not a dream or illusion or\x01",
            "some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x1A,
        "#1310F#6PDid you not consider those possibilities?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x1C,
        "#052F#5PWell, sure, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #325
        0x18,
        (
            "#1547F#6PAh, I think I have our answer.\x02\x03",

            "#1541FThe warmth of Tita's embrace coupled with\x01",
            "her unique juvenile scent were just too real\x01",
            "to leave room for doubt in his heart.\x02\x03",

            "Not to worry! I understand completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x1C,
        "#055F#5P...?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    Sleep(300)
    OP_8C(0x11, 0, 600)

    ChrTalk(    #327
        0x11,
        "#565F#6PWh-Wh-Wha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x12,
        "#179F#6PHmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x16,
        (
            "#1380F#6PI... Umm...\x02\x01",

            "#1165FI kinda get what he means...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #330
        0x1C,
        (
            "#055F#5PWhoa, there! You guys aren't buyin' HIS stock,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x1B,
        (
            "#1521F#12PNow, now. There's no need to get so flustered...\x01",
            "or try and deny it. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x14,
        (
            "#210F#6PNo one's judging you here. Couples come in\x01",
            "all shapes and sizes. Your age gap's just a\x01",
            "little bigger than the average one's, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x1A,
        (
            "#1311F#5PIn fact, the age gap's what makes it all so CUTE!\x02\x03",

            "#1314FYou're so close, and yet that's what separates\x01",
            "you juuust enough to make your relationship that\x01",
            "much more sweet yet thrilling to watch unfold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x14,
        (
            "#415F#6PWhen you put it like that, yeah. I can see the\x01",
            "appeal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x11,
        "#562F#6PU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #336
        0x1C,
        (
            "#057F#5PSo, show of hands--which of you assholes\x01",
            "wants my sword in their face first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x13,
        (
            "#277F#6P(You wouldn't think we were in a perilous \x01",
            "situation looking at them, would you?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x19,
        "#071F#11P(Haha. This is just our way, really.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x1C,
        (
            "#551F#5PAhhh, forget it. Can we just get to work?\x02\x03",

            "#552F...Actually, wait. Didn't you say you have\x01",
            "another companion?\x02\x03",

            "The sister. Where'd she go, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "#063F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x109,
        (
            "#1840F#6P...Sorry. She's over in the library area at the\x01",
            "moment, but she's, uh...not part of the group\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EC07():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC07)
    Sleep(50)

    def lambda_EC1A():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EC1A)
    Sleep(50)
    OP_8C(0x1A, 315, 400)
    Sleep(300)

    ChrTalk(    #342
        0x1A,
        (
            "#816F#11PHer name's Ries, right?\x02\x03",

            "#811FI stopped to talk with her a while ago,\x01",
            "and couldn't believe how adorable she\x01",
            "was. I wish we could've talked more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x1B,
        (
            "#1527F#12PI stayed and spoke with her for a short while,\x01",
            "too. She has such a unique aura about her.\x02\x03",

            "She didn't seem very cheerful, though, so it\x01",
            "was mostly me doing the talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        (
            "#1505F#6P...Kevin?\x02\x03",

            "#1503FAre you sure you don't want to go and sit with\x01",
            "her for a while? I can handle leading the group\x01",
            "if you want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x109,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 225, 400)
    Sleep(300)

    ChrTalk(    #346
        0x109,
        (
            "#1078F#5PThanks for the offer, Joshua, but that's probably\x01",
            "not the best idea. I seem to be the best at handling\x01",
            "the cube, for one thing.\x02\x03",

            "Then there's a pretty good chance we'll run into\x01",
            "more devils, and then you're gonna want my help...\x01",
            "so I think I'm better staying in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x102,
        "#1503F#6PStill...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x109,
        (
            "#1075F#5PIt's all right. She'll cheer up on her own eventually.\x01",
            "She's not a kid anymore.\x02\x03",

            "#1840FAnyway, I think we'd better get going. It's not like\x01",
            "we have all the time in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x16,
        "#1163F#6PWell, if you're sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x18,
        (
            "#1545F#6PIn that case, maybe I should stay behind and\x01",
            "gently pry open the door to her heart.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F0B6():
        OP_6D(1500, 4000, -2600, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_F0B6)

    def lambda_F0CE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F0CE)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_0D()

    def lambda_F0F6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F0F6)

    def lambda_F104():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F104)
    Sleep(50)

    def lambda_F117():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F117)

    def lambda_F125():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F125)
    Sleep(50)

    def lambda_F138():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_F138)

    def lambda_F146():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_F146)
    Sleep(50)

    def lambda_F159():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F159)
    OP_8C(0x1A, 225, 400)
    OP_22(0xBE, 0x0, 0x64)

    def lambda_F173():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_F173)
    WaitChrThread(0x18, 0x0)

    ChrTalk(    #351
        0x18,
        (
            "#1547F#5PI am sure my lute will be the perfect tool for\x01",
            "the job!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x18, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #352
        0x13,
        "#274F#6PJust. Stop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x1B,
        "#1525F#11PYou're never going to grow up, are you?\x02",
    )

    CloseMessageWindow()

    def lambda_F339():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F339)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_63(0x18)
    OP_44(0x109, 0x0)
    OP_A2(0x290E)
    OP_28(0x34, 0x1, 0x8)
    OP_28(0x34, 0x1, 0x10)
    OP_3F(0x35C, 1)
    OP_DB(0x0, 0x5)
    OP_A2(0x25CB)
    Call(6, 15)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_13_D01E end

    SaveToFile()

Try(main)
