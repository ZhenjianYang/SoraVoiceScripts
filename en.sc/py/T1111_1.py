from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1111_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_18E",          # 01, 1
        "Function_2_88D",          # 02, 2
        "Function_3_CD0",          # 03, 3
        "Function_4_D24",          # 04, 4
        "Function_5_EF4",          # 05, 5
        "Function_6_3B81",         # 06, 6
        "Function_7_3BC8",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_104")
    Call(1, 1)
    Jump("loc_187")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 2)
    Jump("loc_187")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_122")
    Call(1, 3)
    Jump("loc_187")

    label("loc_122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_131")
    Call(1, 4)
    Jump("loc_187")

    label("loc_131")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_187")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_18E(): pass

    label("Function_1_18E")

    EventBegin(0x0)
    Fade(1000)
    SetChrSubChip(0x8, 1)
    SetChrPos(0x101, -119000, 0, 68680, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE")
    SetChrPos(0xF8, -118380, 0, 69420, 270)
    SetChrPos(0xF7, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)
    Jump("loc_2A7")

    label("loc_1EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231")
    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF8, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)
    Jump("loc_2A7")

    label("loc_231")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_274")
    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF9, -117250, 0, 68490, 270)
    SetChrPos(0xF8, -118000, 0, 67990, 270)
    Jump("loc_2A7")

    label("loc_274")

    SetChrPos(0xF7, -118380, 0, 69420, 270)
    SetChrPos(0xF8, -117250, 0, 68490, 270)
    SetChrPos(0xF9, -118000, 0, 67990, 270)

    label("loc_2A7")

    OP_6D(-119770, 0, 69530, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_4CB")

    ChrTalk(    #1
        0x8,
        (
            "#612FEveryone. I wonder...\x02\x03",

            "Have you shown that photograph\x01",
            "to Lila yet?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_45F")

    ChrTalk(    #2
        0x101,
        "#1011FYeah, we had her look at it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "#612FDid you now... Did she say anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1015FYeah, she REALLY freaked out for a\x01",
            "moment when she saw it.\x02\x03",

            "She didn't say much of anything, though.\x02\x03",

            "#1002FThough it was SO obvious she was hiding\x01",
            "something it almost hurt.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_4C8")

    label("loc_45F")


    ChrTalk(    #5
        0x101,
        "#1002FNot yet, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#612FAs I said, do that first.\x02\x03",

            "I think you may obtain a clue\x01",
            "of some kind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8")

    Jump("loc_885")

    label("loc_4CB")

    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x8,
        (
            "#613F*gasp* This is...!\x02\x03",

            "Estelle, where in the world did you\x01",
            "get this picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1015FUh, well...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Estelle explained that the group was looking for Corna's\x01",
            "niece, who went missing in the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #10
        0x8,
        (
            "#618FIs...that so...?\x02\x03",

            "Why has this come up now,\x01",
            "of all times...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1002FWhy do I get the feeling you\x01",
            "have some idea of what's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#615FI... I may, at that.\x02\x03",

            "#612FOut of curiosity. Have you shown that\x01",
            "photograph to Lila yet?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_80B")

    ChrTalk(    #13
        0x101,
        (
            "#1011FYeah, actually, we showed it to her\x01",
            "a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "#612FDid you, now...? Did she say anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1015FYeah, she REALLY freaked out for a\x01",
            "moment when she saw it.\x02\x03",

            "She didn't say much of anything, though.\x02\x03",

            "#1002FThough it was SO obvious she was hiding\x01",
            "something it almost hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x10)
    Call(1, 5)
    Jump("loc_885")

    label("loc_80B")


    ChrTalk(    #16
        0x101,
        (
            "#1011FTo Lila?\x02\x03",

            "#1000FNo, not yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#612FDo that first, then.\x02\x03",

            "I think you may obtain a clue\x01",
            "of some kind.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x4)

    label("loc_885")

    SetChrSubChip(0x8, 0)
    EventEnd(0x4)
    Return()

    # Function_1_18E end

    def Function_2_88D(): pass

    label("Function_2_88D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_928")

    ChrTalk(    #18
        0x9,
        (
            "#620FI am in the middle of cleaning.\x02\x03",

            "I am sincerely sorry, but if you have\x01",
            "business with me, it will have to wait\x01",
            "for another time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_928")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x9,
        (
            "#628F*gasp*\x02\x03",

            "Th-Th-Tha-that p-picture...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1015FUh... yeah. You see--\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Estelle explained that the group was looking for Corna's\x01",
            "niece, who went missing in the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #22
        0x9,
        (
            "#627FI...\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1002FDo you have any idea who's in this photo?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #24
        0x9,
        "#624FNo... I'm afraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002F... You're sure?\x02\x03",

            "You looked just a BIT surprised\x01",
            "when you saw it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_C1F")

    ChrTalk(    #26
        0x9,
        (
            "#620FYes, I was struck by how much that girl\x01",
            "resembles an acquaintance.\x02\x03",

            "I was a little unsure if it was her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015FOh, okay...\x02\x03",

            "Sorta odd, though.\x02\x03",

            "Mayor Maybelle said you might have some kind\x01",
            "of clue for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#620FIs that so?\x02\x03",

            "I'm sorry, but I must get back to work.\x02\x03",

            "Please, pardon me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC6")

    label("loc_C1F")


    ChrTalk(    #29
        0x9,
        (
            "#620FYes, I was struck by how much that girl\x01",
            "resembles an acquaintance.\x02\x03",

            "I was a little unsure if it was her.\x02\x03",

            "I'm sorry, but I must get back to work.\x01",
            "Pardon me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC6")

    OP_28(0x79, 0x1, 0x8)

    label("loc_CCC")

    TalkEnd(0x9)
    Return()

    # Function_2_88D end

    def Function_3_CD0(): pass

    label("Function_3_CD0")

    TalkBegin(0xB)

    ChrTalk(    #30
        0xB,
        "Ah, what a cute child!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "I wish I'd been that cute\x01",
            "when I was young!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_3_CD0 end

    def Function_4_D24(): pass

    label("Function_4_D24")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DBB")

    ChrTalk(    #32
        0xC,
        (
            "I distinctly remember seeing another\x01",
            "picture of the girl shown here in the\x01",
            "master's study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "I do wonder who it was a picture of.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EF0")

    label("loc_DBB")


    ChrTalk(    #34
        0xC,
        "Oh? This photograph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1004FYou recognize it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #36
        0xC,
        (
            "I do not recall this photograph precisely,\x01",
            "no. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "I distinctly remember seeing another\x01",
            "picture of the girl shown here in the\x01",
            "master's study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xC,
        "I do wonder who it was a picture of.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        "Perhaps you could find something there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_EF0")

    TalkEnd(0xC)
    Return()

    # Function_4_D24 end

    def Function_5_EF4(): pass

    label("Function_5_EF4")

    SetChrSubChip(0x8, 0)

    ChrTalk(    #40
        0x8,
        (
            "#615FI see.\x01",
            "Blast it, Lila, why...\x02\x03",

            "*sigh* I suppose it falls to me to explain.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x101,
        (
            "#1011FEr, I think I'm a little lost.\x02\x03",

            "You know the girl in the picture?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x3E8)
    Sleep(400)

    ChrTalk(    #42
        0x8,
        (
            "#618FOf course I do.\x01",
            "I've known the girl in that picture for\x01",
            "ages, and she's...very important to me.\x02\x03",

            "Because the girl in that picture...\x01",
            "is Lila.\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x53)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x101,
        "#1004FSay WHAT?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(    #44
        0x105,
        "#044FOh, my!\x02",
    )

    CloseMessageWindow()

    label("loc_10B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D5")

    ChrTalk(    #45
        0x107,
        "#064FReally?!\x02",
    )

    CloseMessageWindow()

    label("loc_10D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112E")

    ChrTalk(    #46
        0x104,
        (
            "#033FOho...\x02\x03",

            "The orchestra hits, as a truth\x01",
            "is revealed to the stage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1165")

    ChrTalk(    #47
        0x108,
        "#073FCertainly not what I expected!\x02",
    )

    CloseMessageWindow()

    label("loc_1165")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D0")

    ChrTalk(    #48
        0x109,
        (
            "#1064FThink even the Goddess'd be surprised at\x01",
            "that one. And she's, y'know, omniscient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D0")


    ChrTalk(    #49
        0x101,
        "#1004FUmmm... you're sure?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(    #50
        0x8,
        (
            "#612FCompletely and absolutely.\x02\x03",

            "#615FLila came to our home on a certain day\x01",
            "ten years ago.\x02\x03",

            "The day the army of Erebonia began its\x01",
            "assault on the city of Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1026FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#618FWhen Father returned after assisting in the\x01",
            "evacuation of much of the citizenry, he had\x01",
            "a girl with him.\x02\x03",

            "Father would only say that she had been\x01",
            "entrusted to him by strangers.\x02\x03",

            "That girl was Lila.\x01",
            "Now that I look, she was even wearing the same\x01",
            "clothes then, though they were bloody and torn.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1444")

    ChrTalk(    #53
        0x103,
        (
            "#022FThat more or less matches Corna's\x01",
            "testimony.\x02\x03",

            "I think we have our answer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1680")

    label("loc_1444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D0")

    ChrTalk(    #54
        0x106,
        (
            "#050FYeah, that matches Corna's story, and\x01",
            "even fills in some of the gaps 'n questions.\x02\x03",

            "Looks like we have our girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1680")

    label("loc_14D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155D")

    ChrTalk(    #55
        0x108,
        (
            "#074FIt all matches Corna's testimony,\x01",
            "and even explains some of the questions.\x02\x03",

            "#072FI believe we have found 'Raini.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1680")

    label("loc_155D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FE")

    ChrTalk(    #56
        0x104,
        (
            "#030FMuch of this matches what Corna told us,\x01",
            "and it even answers a few lingering\x01",
            "questions.\x02\x03",

            "Our wayward orphan has been found,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1680")

    label("loc_15FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1680")

    ChrTalk(    #57
        0x109,
        (
            "#1063FYeah, that pretty much matches what Corna\x01",
            "told us, and it fills in a few gaps.\x02\x03",

            "Think we found our girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1680")


    ChrTalk(    #58
        0x101,
        (
            "#1015FOne thing, though: the names.\x02\x03",

            "We're looking for a girl named Raini,\x01",
            "not Lila.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#613FRaini?\x02\x03",

            "So that was Lila's old name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1002FEr, yeah, that's what Corna told us,\x01",
            "at least.\x02\x03",

            "Hang on, you didn't know Lila's real name,\x01",
            "Mayor Maybelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#618FNo, she never told us...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(    #62
        0x106,
        (
            "#052FWait a tick.\x01",
            "She didn't tell you her name?\x02\x03",

            "She was ten years old. Can't imagine\x01",
            "she didn't know her own name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A30")

    label("loc_182C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")

    ChrTalk(    #63
        0x104,
        (
            "#033FWait a moment, she did not give you\x01",
            "her name?\x02\x03",

            "I cannot imagine she did not know her\x01",
            "own name at that age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A30")

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(    #64
        0x108,
        (
            "#073FShe did not name herself?\x02\x03",

            "I find it hard to believe she did not\x01",
            "know her own name at that age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A30")

    label("loc_192D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B4")

    ChrTalk(    #65
        0x103,
        (
            "#023FWait, I'm a little confused.\x01",
            "She didn't give you her name?\x02\x03",

            "Surely she knew her own name at the\x01",
            "age of ten?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A30")

    label("loc_19B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(    #66
        0x109,
        (
            "#1064FEr, wait, she never gave you her name?\x02\x03",

            "How's THAT work?\x01",
            "Figure she'd know her own name, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A30")


    ChrTalk(    #67
        0x8,
        (
            "#618FI wish she could've given us her name...\x01",
            "or anything, in those days.\x02\x03",

            "When Lila came to live with us, she could\x01",
            "barely say anything at all.\x02\x03",

            "How can I even describe it?\x02\x03",

            "It was as if she was in a state where\x01",
            "she'd forgotten how to speak entirely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1020FHow would that even...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C5F")

    ChrTalk(    #69
        0x109,
        (
            "#1067FSon of a... Medically, we call it\x01",
            "temporary aphasia.\x02\x03",

            "It's when you lose the ability to speak.\x01",
            "It can be caused by extreme mental trauma,\x01",
            "like seeing your...\x02\x03",

            "A girl like her had to see something so\x01",
            "horrible it took her ability to speak...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2005")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D45")

    ChrTalk(    #70
        0x108,
        (
            "#072FI have heard that extreme mental shock can\x01",
            "temporarily rob one of the ability to speak.\x02\x03",

            "And if something terrible were to happen\x01",
            "to a child...\x02\x03",

            "Dragons give her strength.\x01",
            "What did she witness that day?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2005")

    label("loc_1D45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E52")

    ChrTalk(    #71
        0x104,
        (
            "#032FExtremes of duress can cause one to lose\x01",
            "the ability to speak.\x02\x03",

            "I know of all too many examples of that\x01",
            "happening, courtesy of the horrors of\x01",
            "war.\x02\x03",

            "For a ten-year-old girl to experience\x01",
            "the same horrors that silenced soldiers...\x01",
            "Unspeakable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2005")

    label("loc_1E52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F34")

    ChrTalk(    #72
        0x103,
        (
            "#522FShock can cause loss of speech, in severe\x01",
            "cases.\x02\x03",

            "I've heard it can be prevalent in victims\x01",
            "of terrible battles in war...\x02\x03",

            "Aidios' mercy. Just thinking about what\x01",
            "she must have seen makes me shiver.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2005")

    label("loc_1F34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2005")

    ChrTalk(    #73
        0x106,
        (
            "#053FI've heard of this happening to soldiers\x01",
            "and folks in wars.\x02\x03",

            "You get into a bad enough fight, you see\x01",
            "enough horrible stuff, and...\x02\x03",

            "#552FThat goddamn war messed up everyone's\x01",
            "lives...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2005")


    ChrTalk(    #74
        0x8,
        (
            "#615FYes, her soul was far more hurt than her\x01",
            "body when she came to live with us.\x02\x03",

            "We all tried our best, but Lila always\x01",
            "kept a little distance between herself\x01",
            "and everyone else.\x02\x03",

            "So we never learned her true name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1002FSo how'd she get the name 'Lila,' then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#612FFather gave it to her.\x02\x03",

            "It was inconvenient, to say the least,\x01",
            "for her to remain nameless.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21DC")

    ChrTalk(    #77
        0x103,
        (
            "#026FI see, I think we understand now.\x02\x03",

            "All that's left then is to ask her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238E")

    label("loc_21DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(    #78
        0x106,
        (
            "#053FI see. I think we get it.\x02\x03",

            "Only thing to do now is just ask her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238E")

    label("loc_2238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229A")

    ChrTalk(    #79
        0x108,
        (
            "#074FI believe we understand now.\x02\x03",

            "We must ask Lila about this again, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238E")

    label("loc_229A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231D")

    ChrTalk(    #80
        0x104,
        (
            "#032FAnd all of the pieces of the puzzle fall\x01",
            "into place.\x02\x03",

            "All that remains is to assemble them\x01",
            "before Lila.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238E")

    label("loc_231D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238E")

    ChrTalk(    #81
        0x105,
        (
            "#042FNow I see... I believe we understand.\x02\x03",

            "The only thing we can do now is ask\x01",
            "Lila again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238E")


    ChrTalk(    #82
        0x8,
        (
            "#615FYes, there's only one thing to do...\x02\x03",

            "#612FLet me get Sarah to bring her here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -120720, 0, 66270, 135)
    SetChrPos(0x101, -121860, 0, 65600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2466")
    SetChrPos(0xF8, -121860, 0, 64500, 90)
    SetChrPos(0xF9, -122900, 0, 65080, 90)
    SetChrPos(0xF7, -122900, 0, 66180, 90)
    Jump("loc_251F")

    label("loc_2466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A9")
    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF9, -122900, 0, 65080, 90)
    SetChrPos(0xF8, -122900, 0, 66180, 90)
    Jump("loc_251F")

    label("loc_24A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EC")
    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF8, -122900, 0, 65080, 90)
    SetChrPos(0xF9, -122900, 0, 66180, 90)
    Jump("loc_251F")

    label("loc_24EC")

    SetChrPos(0xF7, -121860, 0, 64500, 90)
    SetChrPos(0xF8, -122900, 0, 65080, 90)
    SetChrPos(0xF9, -122900, 0, 66180, 90)

    label("loc_251F")

    OP_6D(-120720, 0, 66270, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 255)
    OP_67(0, 4710, -10000, 0)
    OP_6B(3000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0xB, -118000, 0, 62730, 0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x9, -118000, 0, 62730, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x40)
    OP_43(0xB, 0x0, 0x1, 0x7)
    OP_43(0x9, 0x0, 0x1, 0x6)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #83
        0xB,
        "I've brought her, milady.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)

    ChrTalk(    #84
        0x8,
        (
            "#610F#6PThank you, Sarah.\x01",
            "Would you leave us for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        "Of course, pardon me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    OP_8E(0xB, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)

    def lambda_265E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_265E)
    OP_8E(0xB, 0xFFFE3310, 0x0, 0xF50A, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)

    def lambda_2689():

        label("loc_2689")

        TurnDirection(0x8, 0x9, 0)
        OP_48()
        Jump("loc_2689")

    QueueWorkItem2(0x8, 1, lambda_2689)

    ChrTalk(    #86
        0x8,
        "#612F#6PLila, come here.\x02",
    )

    CloseMessageWindow()

    def lambda_26B8():
        OP_6D(-121200, 0, 66520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B8)
    OP_8E(0x9, 0xFFFE2ED8, 0x0, 0x102DE, 0x7D0, 0x0)
    TurnDirection(0x9, 0x8, 400)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)

    ChrTalk(    #87
        0x9,
        (
            "#620FWhat would you ask of me,\x01",
            "Miss Maybelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#615F#6POur bracer friends showed me this\x01",
            "photograph.\x02\x03",

            "That's certainly a familiar face,\x01",
            "isn't it?\x02\x03",

            "#612FLila...this is you, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        "#620F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#612F#6PI think I can guess why you're remaining\x01",
            "quiet.\x02\x03",

            "You're concerned about Father, aren't you?\x02\x03",

            "I know you feel as though you owe Father\x01",
            "a great debt.\x02\x03",

            "#615FBut, Lila...\x02\x03",

            "I don't want that to be a burden on your\x01",
            "life. And I know he wouldn't, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#624FA burden...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#612F#6PYes, it's why you haven't said anything\x01",
            "about this all this time, isn't it?\x02\x03",

            "You feel obligated to remain here out of\x01",
            "debt to what Father did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "#627FThat is...well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#615F#6PFather said it often, didn't he?\x02\x03",

            "'Those trapped by the shackles of the\x01",
            "past can never blaze a new trail.'\x02\x03",

            "#612FLila, you've done more for our family\x01",
            "than could ever have been expected or\x01",
            "asked of you.\x02\x03",

            "You don't need to keep shackling yourself\x01",
            "to the past.\x02\x03",

            "Go meet this Corna woman.\x02\x03",

            "Meet her and reclaim your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#620F...\x02\x03",

            "Miss Maybelle... I understand what\x01",
            "you're trying to say.\x02\x03",

            "#621FUnfortunately, however...\x02\x03",

            "The Raini you are searching for is\x01",
            "no longer with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1026F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "#613F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#620FRaini was killed in the Hundred Days War,\x01",
            "alongside her parents.\x02\x03",

            "She rests peacefully somewhere in this\x01",
            "land.\x02\x03",

            "That is what I've told myself all these\x01",
            "years.\x02\x03",

            "#625FBecause... Because if I didn't,\x01",
            "it would be too sad, too lonely to...\x01",
            "to bear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        "#618F#6POh, Lila...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1026F#6PLila...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#618F#6PI can't believe this...\x02\x03",

            "I've been such an idiot.\x02\x03",

            "You've been bearing all this within\x01",
            "you all this time. I should've...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #102
        0x101,
        (
            "#1010F#6P...\x02\x03",

            "#1025FUm, Lila?\x02\x03",

            "I don't think you need to lie to yourself\x01",
            "any more. Don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        "#620FI'm sorry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1000F#6PMayor Maybelle, Sarah...\x02\x03",

            "Mayner, the people of the market,\x01",
            "I bet a lot of others around town,\x01",
            "too...\x02\x03",

            "Everyone thinks of you as part of\x01",
            "their family, Lila.\x02\x03",

            "There's no way you're alone any\x01",
            "more.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #105
        0x8,
        "#613F#4PEstelle...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EEE")

    ChrTalk(    #106
        0x103,
        "#020FIndeed.\x02",
    )

    CloseMessageWindow()

    label("loc_2EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F1E")

    ChrTalk(    #107
        0x107,
        "#060FYeah, Estelle is right!\x02",
    )

    CloseMessageWindow()

    label("loc_2F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4B")

    ChrTalk(    #108
        0x105,
        "#047FI think so, as well.\x02",
    )

    CloseMessageWindow()

    label("loc_2F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F77")

    ChrTalk(    #109
        0x106,
        "#051FHeh, damn straight.\x02",
    )

    CloseMessageWindow()

    label("loc_2F77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FDB")

    ChrTalk(    #110
        0x109,
        (
            "#1060FGot that right!\x01",
            "The bonds between people're\x01",
            "stronger than you might think!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3045")

    ChrTalk(    #111
        0x108,
        (
            "#070FYes, I agree!\x02\x03",

            "It may simply be my humble opinion,\x01",
            "but you are hardly alone here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30AD")

    ChrTalk(    #112
        0x104,
        (
            "#031FHeh, indeed.\x02\x03",

            "If nothing else, you have the passionate\x01",
            "love of Olivier Lenheim!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AD")

    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #113
        0x8,
        (
            "#612F#6PLila, are you listening?\x01",
            "Do you see what they mean?\x02\x03",

            "#615FYou're one of the most...\x02\x03",

            "No. With Father gone, you...\x01",
            "you're THE most precious, important\x01",
            "person in my life.\x02\x03",

            "#618FSo saying you're alone like that...\x02\x03",

            "Please, please don't say something so\x01",
            "terribly sad. You've NEVER been alone,\x01",
            "Lila. Ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        "#627FMiss Maybelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#615F#6PAnd, Lila...\x02\x03",

            "Lying to yourself to forget something\x01",
            "painful?\x02\x03",

            "It's exactly what Father hated to see.\x01",
            "Someone trapped by their past...\x02\x03",

            "#612FFather entrusted us both with such a\x01",
            "valuable lesson... Please, don't let it\x01",
            "go to waste.\x02\x03",

            "Lila, go meet Corna. Please.\x02\x03",

            "Or does what Father taught us mean\x01",
            "so little to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "#627FI...\x02\x03",

            "#623FVery well... I'll accept defeat.\x02\x03",

            "*sigh* Miss Maybelle, you're terrible.\x02\x03",

            "How is anyone meant to say no to an\x01",
            "argument like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#610F#6PThat, my dear Lila, is the secret to\x01",
            "driving a hard bargain.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3464")

    ChrTalk(    #118
        0x108,
        "#070FAll right! That's that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3584")

    label("loc_3464")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B5")

    ChrTalk(    #119
        0x106,
        (
            "#051FAlways good to see a happy ending\x01",
            "to stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3584")

    label("loc_34B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FA")

    ChrTalk(    #120
        0x103,
        (
            "#027FAhh, happy endings always warm\x01",
            "the heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3584")

    label("loc_34FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354A")

    ChrTalk(    #121
        0x104,
        (
            "#031FAnd our small side drama reaches a\x01",
            "happy conclusion!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3584")

    label("loc_354A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3584")

    ChrTalk(    #122
        0x109,
        "#1060FI'd say that takes care of that!\x02",
    )

    CloseMessageWindow()

    label("loc_3584")


    ChrTalk(    #123
        0x101,
        "#1007F#6PPhew! Good to see that's all settled.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #124
        0x8,
        (
            "#617F#4PYes, I'm glad.\x02\x03",

            "#611FCome on, then!\x01",
            "Let's go meet her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#622FP-Pardon?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #126
        0x101,
        (
            "#1011F#6PGo meet...\x02\x03",

            "Er, you're coming, Mayor Maybelle?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D5")

    ChrTalk(    #127
        0x106,
        (
            "#051FHey, it's cool.\x02\x03",

            "She's basically going to be representing\x01",
            "her old man. I can get behind that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CA")

    label("loc_36D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3748")

    ChrTalk(    #128
        0x103,
        (
            "#020FI don't think it's a problem.\x02\x03",

            "With her father passed away, she has to\x01",
            "go in his stead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CA")

    label("loc_3748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C6")

    ChrTalk(    #129
        0x108,
        (
            "#070FIt should be all right, I think.\x02\x03",

            "Her father has passed away, so she must\x01",
            "represent him in spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CA")

    label("loc_37C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3866")

    ChrTalk(    #130
        0x104,
        (
            "#030FI see no issue.\x02\x03",

            "In all other regards, Mayor Maybelle fills\x01",
            "her father's shoes well. It is only right\x01",
            "she should do so now, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CA")

    label("loc_3866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38CA")

    ChrTalk(    #131
        0x109,
        (
            "#1060FI think it's cool, y'know?\x02\x03",

            "She'll be there in her father's stead\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CA")


    ChrTalk(    #132
        0x8,
        "#611F#4PYes, yes, precisely!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #133
        0x8,
        "#610F#6PCome on, Lila, let's be off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "#621F...All right.\x02\x03",

            "I'll accompany you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "#617F#6POh, no, you don't. I'M the one 'accompanying'\x01",
            "YOU this time.\x02\x03",

            "Come on, get in front of me.\x01",
            "Left, right, left, right, let's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFE2C30, 0x0, 0x102F2, 0x7D0, 0x0)
    OP_8C(0x9, 135, 400)

    def lambda_39FD():
        OP_8E(0x8, 0xFFFE2D3E, 0x0, 0x10284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_39FD)

    def lambda_3A18():
        OP_8E(0x9, 0xFFFE30C2, 0x0, 0x100E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A18)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x9, 0x0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #136
        0x9,
        "#623F#4PBut, but, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1001FHahaha. It's okay, Lila.\x02\x03",

            "After all, you're the star this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#611F#3PPrecisely! See?\x01",
            "Listen to the smart bracer lady.\x02\x03",

            "Coooome on, hurry now.\x01",
            "I'll be right behind you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #139
        0x9,
        "#626F#4PMaybeeeeeelle...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x79, 0x1, 0x20)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_EF4 end

    def Function_6_3B81(): pass

    label("Function_6_3B81")

    Sleep(1500)

    def lambda_3B8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B8C)
    OP_8E(0xFE, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE319E, 0x0, 0xFE69, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_6_3B81 end

    def Function_7_3BC8(): pass

    label("Function_7_3BC8")


    def lambda_3BCE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BCE)
    OP_8E(0xFE, 0xFFFE3310, 0x0, 0xFC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE2F82, 0x0, 0xFC12, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_7_3BC8 end

    SaveToFile()

Try(main)
