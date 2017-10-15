from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        Unknown_30              = 35,
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
        "Function_1_5F3",          # 01, 1
        "Function_2_1714",         # 02, 2
        "Function_3_17C5",         # 03, 3
        "Function_4_1E16",         # 04, 4
        "Function_5_413D",         # 05, 5
        "Function_6_4490",         # 06, 6
        "Function_7_52FF",         # 07, 7
        "Function_8_54E8",         # 08, 8
        "Function_9_59D9",         # 09, 9
        "Function_10_68BE",        # 0A, 10
        "Function_11_745D",        # 0B, 11
        "Function_12_7D8A",        # 0C, 12
        "Function_13_8F92",        # 0D, 13
        "Function_14_9791",        # 0E, 14
        "Function_15_9B07",        # 0F, 15
        "Function_16_9C45",        # 10, 16
        "Function_17_9FFD",        # 11, 17
        "Function_18_A50C",        # 12, 18
        "Function_19_AA8A",        # 13, 19
        "Function_20_B590",        # 14, 20
        "Function_21_BF04",        # 15, 21
        "Function_22_C103",        # 16, 22
        "Function_23_CA09",        # 17, 23
        "Function_24_D07A",        # 18, 24
        "Function_25_DB51",        # 19, 25
        "Function_26_F042",        # 1A, 26
        "Function_27_F050",        # 1B, 27
        "Function_28_F07D",        # 1C, 28
        "Function_29_F0AA",        # 1D, 29
        "Function_30_F0E7",        # 1E, 30
        "Function_31_F124",        # 1F, 31
        "Function_32_F139",        # 20, 32
        "Function_33_F14E",        # 21, 33
        "Function_34_F163",        # 22, 34
        "Function_35_F178",        # 23, 35
        "Function_36_F1BB",        # 24, 36
        "Function_37_F1EF",        # 25, 37
        "Function_38_F223",        # 26, 38
        "Function_39_F257",        # 27, 39
        "Function_40_F28B",        # 28, 40
        "Function_41_F2E4",        # 29, 41
        "Function_42_F2EC",        # 2A, 42
        "Function_43_F2F4",        # 2B, 43
        "Function_44_F31D",        # 2C, 44
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    TurnDirection(0x1, 0xE, 0)
    TurnDirection(0x2, 0xE, 0)
    TurnDirection(0x3, 0xE, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_174")

    ChrTalk(    #0
        0xE,
        (
            "Still, we were most certainly jumping\x01",
            "to conclusions by doubting Kuper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xE,
        (
            "I've got to apologize to him about\x01",
            "all this when I get a chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2")

    label("loc_174")

    OP_A2(0x8)

    ChrTalk(    #2
        0xE,
        "Hello, everyone! Thank you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        (
            "I couldn't have asked for a more\x01",
            "capable team.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2")

    Jump("loc_5F2")

    label("loc_1D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_24B")

    ChrTalk(    #4
        0xE,
        "Hello, bracers! Excellent work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "If anything else happens,\x01",
            "I'll make sure to call on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F2")

    label("loc_24B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_260")
    Jump("loc_277")

    label("loc_260")


    ChrTalk(    #6
        0xE,
        "Why, hello there.\x02",
    )

    CloseMessageWindow()

    label("loc_277")


    ChrTalk(    #7
        0xE,
        (
            "Would it be possible for you to\x01",
            "look into things now, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")

    ChrTalk(    #8
        0x101,
        "#1006FSure, no problem.\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #9
        0xE,
        "Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        "Thanks! I owe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xE,
        "Now, come on in. I'll introduce you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 4)
    OP_A2(0xA)
    Jump("loc_452")

    label("loc_3B9")


    ChrTalk(    #12
        0x101,
        (
            "#1007FS-Sorry...\x02\x03",

            "We can't right this second.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #13
        0xE,
        "Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "That's fine, I suppose. I'll just wait\x01",
            "for a different bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_8C(0xE, 90, 0)

    label("loc_452")

    Jump("loc_5F2")

    label("loc_455")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #15
        0xE,
        (
            "They're in the middle of a very critical\x01",
            "meeting, so I'm afraid I can't let you\x01",
            "pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xE,
        (
            "I'm sorry, but if you have business,\x01",
            "please come again another time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB")

    label("loc_50F")

    OP_A2(0x8)

    ChrTalk(    #17
        0xE,
        (
            "Welcome to Candidate Norman's\x01",
            "election office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        (
            "They're in the middle of a very critical\x01",
            "meeting, so I'm afraid I can't let you\x01",
            "pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xE,
        (
            "I'm sorry, but if you have business,\x01",
            "please come again another time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB")

    OP_8C(0xE, 90, 0)

    label("loc_5F2")

    Return()

    # Function_0_AA end

    def Function_1_5F3(): pass

    label("Function_1_5F3")

    OP_A3(0xA)
    OP_4A(0xE, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16DF")
    TalkBegin(0xE)
    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_644"),
        (1, "loc_794"),
        (2, "loc_A91"),
        (3, "loc_B41"),
        (4, "loc_CA3"),
        (5, "loc_121A"),
        (6, "loc_146C"),
        (7, "loc_15E4"),
        (SWITCH_DEFAULT, "loc_16D6"),
    )


    label("loc_644")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_700")

    ChrTalk(    #20
        0xFE,
        (
            "Kuper looked as shocked as I'd\x01",
            "ever seen him right then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "No surprises there, of course!\x01",
            "I'd be shocked, too, were I caught\x01",
            "right at the scene of the crime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_791")

    label("loc_700")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #22
        0xFE,
        (
            "Kuper's face went white as a sheet\x01",
            "the moment he saw us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "He was surely dismayed at having\x01",
            "been witnessed at the crime scene.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_791")

    Jump("loc_16D9")

    label("loc_794")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_8A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_82D")

    ChrTalk(    #24
        0xFE,
        "I didn't hear any big sound like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I can say for sure that I heard nothing\x01",
            "of the sort while I was there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_82D")


    ChrTalk(    #26
        0xFE,
        "It was completely quiet in the room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "If there were some kind of argument,\x01",
            "I'm sure I would have noticed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0")

    Jump("loc_A8E")

    label("loc_8A3")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #28
        0xFE,
        "W-Well, yes, Kuper's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I was standing in front of the door,\x01",
            "but it was quiet the whole time in\x01",
            "the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If there had been some kind of\x01",
            "argument, I'm sure I would have\x01",
            "noticed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(    #31
        0x101,
        (
            "#1015FBut there's someone who testified\x01",
            "to hearing a big sound.\x02\x03",

            "#1002FHe said it sounded like something\x01",
            "smacking into something else on the\x01",
            "balcony.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #32
        0xFE,
        "Well, I didn't hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I can say for sure that I didn't hear\x01",
            "anything of the like while I was here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8E")

    Jump("loc_16D9")

    label("loc_A91")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_AF2")

    ChrTalk(    #34
        0xFE,
        "Kuper was the same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "He didn't seem to be angry, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3E")

    label("loc_AF2")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #36
        0xFE,
        "Was Kuper angry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "It didn't really look that way, but...\x02",
    )

    CloseMessageWindow()

    label("loc_B3E")

    Jump("loc_16D9")

    label("loc_B41")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(    #38
        0xFE,
        (
            "I'm human, aren't I? Am I not allowed\x01",
            "to look a little unhappy from time to\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I can't imagine why my expression\x01",
            "would have anything to do with the\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0")

    label("loc_BFE")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #40
        0xFE,
        (
            "I had an unpleasant expression,\x01",
            "you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Well, of course! After a fuss like that,\x01",
            "who wouldn't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "What does that have to do with the\x01",
            "case?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0")

    Jump("loc_16D9")

    label("loc_CA3")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E1A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(    #43
        0xFE,
        (
            "Sure, I went up to the second floor,\x01",
            "but I just went to pick up something\x01",
            "I forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "It wasn't anything important, so\x01",
            "I didn't see any reason to make\x01",
            "mention of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E17")

    label("loc_D7A")


    ChrTalk(    #45
        0xFE,
        (
            "After lunch, Norman went to have\x01",
            "a look at the site where he was going\x01",
            "to give a speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I had some stuff I had to do, so I met\x01",
            "up with him later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E17")

    Jump("loc_1217")

    label("loc_E1A")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #47
        0xFE,
        (
            "After lunch, Norman went to have a\x01",
            "look at the site where he was going to\x01",
            "give a speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I had some stuff I had to do, so I met\x01",
            "up with him later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "The rest is as I explained before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_1217")
    OP_28(0x69, 0x1, 0x20)

    ChrTalk(    #50
        0x101,
        (
            "#1002F...But, Herio.\x02\x03",

            "You went to the second floor, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #51
        0xFE,
        "Excuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1002FThere's no point in hiding it.\x01",
            "We have witnesses.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #53
        0xFE,
        "I-I'm not hiding anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I just... I just realized I forgot something\x01",
            "and went back to the office to pick it up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1002FWas there anyone in the office\x01",
            "at that time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "Dels was there doing work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I didn't see anyone else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1000FGreat! That's plenty, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "U-Umm... Don't misunderstand, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I wasn't trying to hide that I'd gone\x01",
            "to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1010FDon't worry. We haven't decided\x01",
            "you're the criminal or anything.\x02\x03",

            "#1002FJust don't forget that this kind of\x01",
            "thing only makes you look worse.\x02\x03",

            "I look forward to your future\x01",
            "assistance, sir.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1217")

    Jump("loc_16D9")

    label("loc_121A")

    OP_28(0x6A, 0x1, 0x400)

    ChrTalk(    #62
        0xFE,
        "I heard the bell toll, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I think it was when I was meeting\x01",
            "with Norman by the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Then Kuper showed up, and\x01",
            "I showed him the way to here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1469")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1433")
    OP_28(0x69, 0x1, 0x200)

    ChrTalk(    #65
        0x101,
        (
            "#1015FSo, you heard the bell when you\x01",
            "were outside, which means...\x02\x03",

            "...you weren't around when that\x01",
            "other big sound happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#042FAccording to the testimony we got,\x01",
            "that big sound happened right after\x01",
            "the bell stopped ringing.\x02\x03",

            "If that's true, then Herio isn't connected\x01",
            "to the big sound that was heard by the\x01",
            "balcony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1469")

    label("loc_1433")


    ChrTalk(    #67
        0x101,
        (
            "#1002FThat matches Norman's testimony,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1469")

    Jump("loc_16D9")

    label("loc_146C")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(    #68
        0xFE,
        (
            "Someone must have done it while\x01",
            "I was out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Normally, it would've been Ernest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E1")

    label("loc_14DA")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #70
        0xFE,
        "Who cleaned up? No idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Someone must have done it while\x01",
            "I was out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1002FWere the plates and such cleaned by\x01",
            "the time you got back to the office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Hmm... I don't know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I wasn't exactly paying attention,\x01",
            "so I can't say for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E1")

    Jump("loc_16D9")

    label("loc_15E4")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1661")

    ChrTalk(    #75
        0xFE,
        (
            "I'm not sure I can help you with\x01",
            "Belden's location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I was out when the bell rang,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D3")

    label("loc_1661")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #77
        0xFE,
        "Where was Belden when the bell rang?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Couldn't tell you, unfortunately.\x01",
            "I was out at the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D3")

    Jump("loc_16D9")

    label("loc_16D6")

    Jump("loc_16D9")

    label("loc_16D9")

    TalkEnd(0xE)
    Jump("loc_170F")

    label("loc_16DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1705")
    EventBegin(0x2)
    Call(1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")
    EventEnd(0x3)

    label("loc_1702")

    Jump("loc_170F")

    label("loc_1705")

    TalkBegin(0xE)
    Call(1, 0)
    TalkEnd(0xE)

    label("loc_170F")

    OP_4B(0xE, 0)
    Return()

    # Function_1_5F3 end

    def Function_2_1714(): pass

    label("Function_2_1714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_171C")
    Return()

    label("loc_171C")

    OP_A3(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1786")
    EventBegin(0x1)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    OP_4A(0xE, 0)
    Call(1, 0)
    OP_4B(0xE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1782")
    OP_8C(0xE, 90, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1783")

    label("loc_1782")

    Return()

    label("loc_1783")

    Jump("loc_17C4")

    label("loc_1786")

    EventBegin(0x1)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    OP_4A(0xE, 255)
    Call(1, 0)
    OP_8C(0xE, 90, 0)
    OP_4B(0xE, 255)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_17C4")

    Return()

    # Function_2_1714 end

    def Function_3_17C5(): pass

    label("Function_3_17C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17CD")
    Return()

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E15")
    EventBegin(0x0)
    OP_4A(0xE, 0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, -2340, 0, 9540, 180)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_28(0x6A, 0x1, 0x8000)
    OP_6D(1780, 0, 2230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 4450, 0, 2400, 270)
    SetChrPos(0xF7, 5150, -50, 1910, 270)
    SetChrPos(0x104, 5700, -550, 2370, 270)
    SetChrPos(0x105, 6350, -1050, 1780, 270)
    OP_43(0x101, 0x1, 0x1, 0x1F)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x1, 0x20)
    Sleep(300)
    OP_43(0x104, 0x1, 0x1, 0x21)
    Sleep(300)
    OP_43(0x105, 0x1, 0x1, 0x22)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #79
        0xE,
        "Man's Voice",
        "Heeey! You guys!\x02",
    )

    CloseMessageWindow()
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1915():

        label("loc_1915")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1915")

    QueueWorkItem2(0x101, 1, lambda_1915)
    Sleep(200)

    def lambda_192B():

        label("loc_192B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_192B")

    QueueWorkItem2(0xF7, 1, lambda_192B)

    def lambda_193C():

        label("loc_193C")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_193C")

    QueueWorkItem2(0x104, 1, lambda_193C)

    def lambda_194D():

        label("loc_194D")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_194D")

    QueueWorkItem2(0x105, 1, lambda_194D)
    OP_6D(-1610, 0, 6840, 2000)

    def lambda_196F():
        OP_6D(-170, 0, 2320, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_196F)
    OP_8E(0xE, 0xFFFFFCCC, 0x0, 0x8E8, 0xBB8, 0x0)
    WaitChrThread(0xE, 0x1)
    TurnDirection(0xE, 0x101, 400)
    WaitChrThread(0xE, 0x2)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)

    ChrTalk(    #80
        0xE,
        "*pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        "Y-You're bracers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1002FYeah. Is something wrong?\x02\x03",

            "You look kinda frazzled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "Th-There's something I'd like\x01",
            "you to investigate urgently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        "Could you come right now?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D08")

    ChrTalk(    #85
        0x101,
        (
            "#1015FHmmm, sorry.\x02\x03",

            "We're just about to head off\x01",
            "for a different region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        "Ah, I see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B5E")

    ChrTalk(    #87
        0x106,
        "#050FDid you contact the guild?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B95")

    label("loc_1B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B95")

    ChrTalk(    #88
        0x103,
        "#022FHave you already contacted the guild?\x02",
    )

    CloseMessageWindow()

    label("loc_1B95")


    ChrTalk(    #89
        0xE,
        "Yeah, just now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        (
            "Oh, well. Guess I have to wait\x01",
            "until another bracer comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1007FYeah, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "We're both busy people.\x01",
            "Not to worry, I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        "If you'll excuse me.\x02",
    )

    CloseMessageWindow()

    def lambda_1C5B():

        label("loc_1C5B")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_1C5B")

    QueueWorkItem2(0x0, 1, lambda_1C5B)

    def lambda_1C6C():

        label("loc_1C6C")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_1C6C")

    QueueWorkItem2(0x1, 1, lambda_1C6C)

    def lambda_1C7D():

        label("loc_1C7D")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_1C7D")

    QueueWorkItem2(0x2, 1, lambda_1C7D)

    def lambda_1C8E():

        label("loc_1C8E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_1C8E")

    QueueWorkItem2(0x3, 1, lambda_1C8E)
    OP_8E(0xE, 0x5DC, 0x0, 0x82, 0x7D0, 0x0)
    OP_8E(0xE, 0x173E, 0x8CA, 0xA0, 0x7D0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8E(0xE, 0x173E, 0x8CA, 0x7B2, 0x7D0, 0x0)
    Sleep(400)
    SetChrPos(0xE, 22470, 0, 76980, 90)
    OP_28(0x6A, 0x1, 0x4000)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    label("loc_1D08")


    ChrTalk(    #94
        0x101,
        "#1006FYeah, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        "Thanks! I owe you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D69")

    ChrTalk(    #96
        0x106,
        "#050FSo, where should we go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(    #97
        0x103,
        "#020FSo, where should we go?\x02",
    )

    CloseMessageWindow()

    label("loc_1D92")


    ChrTalk(    #98
        0xE,
        (
            "Head to Norman's election office.\x01",
            "It's on the top floor of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        "Here, I'll show you the way.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 4)
    EventEnd(0x0)

    label("loc_1E15")

    Return()

    # Function_3_17C5 end

    def Function_4_1E16(): pass

    label("Function_4_1E16")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x0, 1500, 0, 79940, 274)
    SetChrPos(0xB, -3200, 0, 81000, 90)
    SetChrPos(0x14, -2140, 0, 81000, 270)
    OP_6D(-2540, 0, 80960, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    EventBegin(0x0)
    OP_4A(0xB, 0)
    OP_4A(0x14, 0)
    OP_4A(0xE, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #100
        0x14,
        "#4PI'm TELLING YOU, I didn't do it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x14,
        (
            "#4PHurry up and lemme go home!\x01",
            "I've got work to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        "#6PNow, now, calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#6PJust bear with us until the bracers\x01",
            "arrive. Once their investigation's done,\x01",
            "you can leave.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #104
        0xB,
        "#6PSpeak of the devil! See? Here they are.\x02",
    )

    CloseMessageWindow()
    OP_6D(-1280, 0, 79170, 1500)
    OP_43(0xE, 0x1, 0x1, 0x24)
    OP_8C(0x14, 180, 400)
    Sleep(600)

    def lambda_2033():
        OP_6D(-2420, 0, 79460, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2033)
    OP_43(0x101, 0x1, 0x1, 0x25)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2062")
    OP_43(0x106, 0x1, 0x1, 0x26)
    Jump("loc_2070")

    label("loc_2062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2070")
    OP_43(0x103, 0x1, 0x1, 0x26)

    label("loc_2070")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x27)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0x28)
    Sleep(300)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x14, 0x2)
    TurnDirection(0xB, 0xE, 400)

    ChrTalk(    #105
        0xB,
        "That sure was fast, Herio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "Yeah, I lucked out and ran into\x01",
            "some bracers right away.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xE, 215, 400)
    Sleep(400)

    ChrTalk(    #107
        0xE,
        "This is Norman.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        (
            "I'm sure you've seen him on\x01",
            "posters around the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1011F#6POne of the guys running for mayor,\x01",
            "I think?\x02\x03",

            "#1000FI'm Estelle Bright, of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(    #110
        0x106,
        (
            "#050FAgate Crosner, also a bracer.\x02\x03",

            "Let's get to business. What happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2280")

    label("loc_2224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2280")

    ChrTalk(    #111
        0x103,
        (
            "#020FI'm Scherazard Harvey, also a bracer.\x02\x03",

            "So, let's get to it. What happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2280")

    OP_8C(0xB, 180, 400)

    ChrTalk(    #112
        0xB,
        (
            "One of our campaigners, Dels,\x01",
            "was injured by someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        "In other words, it's an assault case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1002F#6PAn assault? Well, that's never a nice\x01",
            "thing to hear.\x02\x03",

            "...Is the victim okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A, 400)
    Sleep(400)

    ChrTalk(    #115
        0xB,
        "#4PYes, he's still here.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #116
        0xB,
        (
            "He was unconscious for a bit,\x01",
            "but it was, thankfully, nothing\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1007F#6PPhew! Good to hear it!\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #118
        0x1A,
        "There's nothin' 'good' about it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x1A,
        (
            "The back of my head still hurts\x01",
            "like you wouldn't believe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1004F#6PThe back of your head, huh?\x02\x03",

            "Were you attacked from behind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1A,
        (
            "Yes, ma'am. Right out of the blue,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x1A,
        (
            "I was taking a breather on the\x01",
            "balcony, and all of a sudden from\x01",
            "behind...THUD.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2564")

    ChrTalk(    #123
        0x106,
        "#057FThat's pretty foul...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2584")

    ChrTalk(    #124
        0x103,
        "#022FHow vicious...\x02",
    )

    CloseMessageWindow()

    label("loc_2584")


    ChrTalk(    #125
        0x101,
        "#1020F#6POuch. Sounds nasty.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2621")

    ChrTalk(    #126
        0x106,
        (
            "#050FWhen did the attack happen?\x02\x03",

            "Give us whatever you can remember\x01",
            "about the events before and after.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2681")

    label("loc_2621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2681")

    ChrTalk(    #127
        0x103,
        (
            "#022FWhen did the incident occur?\x02\x03",

            "Give us any info that happened\x01",
            "before and after.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2681")


    ChrTalk(    #128
        0xE,
        "Sure. It happened today, just after lunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xE,
        (
            "Norman and I were checking out\x01",
            "a potential location for a speech by\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        "Kuper here had just turned up then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "When I talked to him, he said\x01",
            "he had some important business\x01",
            "with Norman.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #132
        0x101,
        "#1002F#6PWhat kind of business?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #133
        0x14,
        (
            "#6PPortos told me to come apologize\x01",
            "for that mess on the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x14,
        (
            "#6PIt's not like it's all my fault,\x01",
            "but I did sort of make it worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1015F#6PI see. So you came to say sorry\x01",
            "for the scuffle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "Yes, but Norman was still very\x01",
            "busy at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xE,
        (
            "We'd asked Kuper to wait in the\x01",
            "office area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        (
            "That's when I showed him\x01",
            "to this room.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #139
        0xB,
        (
            "I returned to the hotel not too\x01",
            "long afterward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "I entered the room with Herio,\x01",
            "who had been waiting outside\x01",
            "the office, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "There was Dels, unconscious\x01",
            "on the balcony.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #142
        0xE,
        "And Kuper was right there.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x14, 400)

    def lambda_2A09():
        TurnDirection(0xB, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A09)

    def lambda_2A17():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2A17)
    OP_6D(-3080, 0, 79610, 1000)

    ChrTalk(    #143
        0xE,
        "Standing over him.\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #144
        0x14,
        (
            "I'm tryin' to tell you, why does\x01",
            "that make ME the criminal?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x14,
        (
            "He was already out cold when\x01",
            "I'd reached the balcony!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "I understand what Kuper's saying,\x01",
            "but it's only natural to suspect him,\x01",
            "given the circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "There was no one in this room\x01",
            "except Kuper and Dels.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #148
        0x101,
        "#1002FIs that true?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #149
        0xE,
        (
            "After I brought Kuper, I was on watch\x01",
            "outside the door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xE,
        "No one entered until Norman got here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "No matter how you look it, that means\x01",
            "these two were alone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C72")
    TurnDirection(0x106, 0x14, 400)

    ChrTalk(    #152
        0x106,
        "#050FYou're sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA6")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2CA6")
    TurnDirection(0x106, 0x14, 400)

    ChrTalk(    #153
        0x103,
        "#022FYou're absolutely positive?\x02",
    )

    CloseMessageWindow()

    label("loc_2CA6")

    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x14, 0xF7, 400)

    ChrTalk(    #154
        0x14,
        "Y-Yeah, it's true, but...it's like I said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x14,
        (
            "When I went out to the balcony,\x01",
            "Dels was already on the ground.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DA1")

    ChrTalk(    #156
        0x106,
        (
            "#052FSo you're saying the crime was\x01",
            "committed before you got there.\x02\x03",

            "Am I gettin' that right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E17")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2E17")

    ChrTalk(    #157
        0x103,
        (
            "#022FSo let me get this straight...\x02\x03",

            "The crime was already committed\x01",
            "by the time you came, is that right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E17")

    OP_62(0x14, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #158
        0x14,
        "YEAH, exactly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x14,
        (
            "Ahh, thank Aidios! Finally, there's\x01",
            "someone who gets it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #160
        0x101,
        (
            "#1015F#6PIn that case, it'd have to be someone\x01",
            "who entered the room before Kuper.\x02\x03",

            "#1002FDels, do you remember anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x1A,
        "It's possible that someone came in...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1A,
        (
            "People go in and out of this office all\x01",
            "the time, though. Even if someone had,\x01",
            "I wouldn't have thought much of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1007F#6PFair enough. It's an election office,\x01",
            "so that makes sense.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30A3")

    ChrTalk(    #164
        0x106,
        (
            "#053FHmm. Sounds simple enough,\x01",
            "at least.\x02\x03",

            "The criminal's gotta be one of\x01",
            "two people:\x02\x03",

            "#057FThis guy here, or someone who\x01",
            "came into the room before him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3163")

    label("loc_30A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3163")

    ChrTalk(    #165
        0x103,
        (
            "#026FMmm... At least we have a good\x01",
            "idea of what's going on.\x02\x03",

            "The culprit behind this attack must\x01",
            "be one of two people:\x02\x03",

            "#027FKuper, or someone who came\x01",
            "before him into this room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3163")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #166
        0x101,
        (
            "#1002FWe should be able to narrow\x01",
            "it down if we get enough proof.\x02\x03",

            "Think we oughtta start questioning?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_32AC")

    ChrTalk(    #167
        0x106,
        (
            "#050FIf there's no other useful information,\x01",
            "yeah.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Sleep(400)

    ChrTalk(    #168
        0x106,
        (
            "#050FIf you guys noticed anythin' else or\x01",
            "are thinking of somethin', tell us now.\x02\x03",

            "Even if it seems like nothing important.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_336F")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_336F")

    ChrTalk(    #169
        0x103,
        (
            "#020FIf there's nothing else to be gleaned\x01",
            "here, yes.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Sleep(400)

    ChrTalk(    #170
        0x103,
        (
            "#020FIf you gentlemen can think of anything\x01",
            "else, please tell me now.\x02\x03",

            "Even if it seems trivial or unimportant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336F")

    Sleep(400)
    TurnDirection(0xB, 0xF7, 400)

    ChrTalk(    #171
        0xB,
        (
            "All right, then I have one more thing\x01",
            "I'd like to add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xB,
        (
            "There was something that occurred to\x01",
            "me as I was looking through the room\x01",
            "after the incident.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #173
        0x101,
        (
            "#1002F#6PWere there signs it'd been rummaged\x01",
            "around in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        "Not at all. Just the opposite, in fact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "It actually felt like it was cleaner\x01",
            "than before.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #176
        0x101,
        "#1004F#6PHuh? Is a serial cleaner on the loose?\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #177
        0x104,
        (
            "#032FHmm... One way to interpret it would\x01",
            "be as a disguise to hide the fact that\x01",
            "the room had been searched.\x02\x03",

            "Of course, it appears they went too far,\x01",
            "inadvertently arousing suspicion in the\x01",
            "process.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #178
        0xB,
        "That's not a bad train of thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        "...Incidentally, who are you?\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x2B)
    Sleep(200)

    ChrTalk(    #180
        0x104,
        (
            "#035FHeh, I was waiting for that question.\x02\x03",

            "I am a traveling bard, a poetic soul\x01",
            "wandering the wilds, a genius mu--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #181
        0x101,
        (
            "#1002F#6PSure, but if nothing's been stolen,\x01",
            "then isn't the idea that it's a disguise\x01",
            "pretty weak?\x02\x03",

            "At this stage, I don't think there's any\x01",
            "point in worrying about motive.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3795")

    ChrTalk(    #182
        0x106,
        "#053F#4PI agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37B2")

    label("loc_3795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_37B2")

    ChrTalk(    #183
        0x103,
        "#026F#4PI agree.\x02",
    )

    CloseMessageWindow()

    label("loc_37B2")

    OP_62(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x104,
        (
            "#035FH-Heh...\x02\x03",

            "You've grown even bolder since our\x01",
            "last rendezvous, Estelle.\x02\x03",

            "Your training at Le Locle was most\x01",
            "fruitful! You're simply stunning.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 400)

    ChrTalk(    #185
        0x105,
        "#045FO-Olivier...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #186
        0x101,
        (
            "#1007FJust ignore him.\x02\x03",

            "#1006FNow, if there's nothing else here\x01",
            "you can tell us, we should get to\x01",
            "questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3965")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #187
        0x106,
        (
            "#052F#4PY-Yeah...\x02\x03",

            "#053F(Well, seems she knows when to\x01",
            "shorten the leash now...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39CD")

    label("loc_3965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_39CD")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #188
        0x103,
        (
            "#023F#4PC-Certainly...\x02\x03",

            "#026F(She's begun to master how to\x01",
            "handle Olivier, I see...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CD")


    ChrTalk(    #189
        0xB,
        "Good luck with the investigation.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A39")
    TurnDirection(0x106, 0xB, 400)

    ChrTalk(    #190
        0x106,
        (
            "#050FWe'll come report once we have\x01",
            "an answer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A7B")

    label("loc_3A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3A7B")
    TurnDirection(0x103, 0xB, 400)

    ChrTalk(    #191
        0x103,
        (
            "#020FWe'll come report once we have\x01",
            "an answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7B")


    ChrTalk(    #192
        0xB,
        (
            "Good. We're counting on you to\x01",
            "get to the bottom of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x18, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 65535)
    ClearChrFlags(0x104, 0x2)
    OP_43(0x104, 0x1, 0x1, 0x2A)
    Sleep(100)
    OP_43(0x101, 0x1, 0x1, 0x2A)
    OP_43(0x105, 0x1, 0x1, 0x2A)
    OP_43(0xF7, 0x1, 0x1, 0x2A)
    OP_69(0x18, 0x3E8)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1002FNow, how should we go about things?\x01",
            "I mean, this hotel is pretty big.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C52")

    ChrTalk(    #194
        0x106,
        (
            "#050FWe should probably split into two\x01",
            "groups.\x02\x03",

            "You and the princess make some\x01",
            "rounds, while I keep an eye on this\x01",
            "dumbass.\x02\x03",

            "These two are our assistants, yeah?\x01",
            "Let's make 'em assist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D01")

    label("loc_3C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3D01")

    ChrTalk(    #195
        0x103,
        (
            "#020FIt's best if we split into two.\x02\x03",

            "Estelle, go with Her Highness.\x01",
            "I'll go with Oliver.\x02\x03",

            "We're lucky to have them as\x01",
            "assistants, so let's make good\x01",
            "use of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D01")


    ChrTalk(    #196
        0x101,
        (
            "#1017FGood point.\x02\x03",

            "Ready to kick some investigation\x01",
            "butt, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x105,
        "#041FHaha, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x104,
        (
            "#031FHeh, assisting companions is only\x01",
            "natural for a hunter of love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1019FYou sure don't miss a beat, do you?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3EC0")

    ChrTalk(    #200
        0x106,
        (
            "#050FAll right, listen up. We need to gather\x01",
            "information on the suspect first.\x02\x03",

            "If you go around asking #4Cabout Kuper,#0C\x01",
            "somethin' should turn up.\x02\x03",

            "If you end up getting a picture on\x01",
            "who our guy is, come tell me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAA")

    label("loc_3EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3FAA")

    ChrTalk(    #201
        0x103,
        (
            "#020FAll right. Our first order of business is\x01",
            "to gather information on the suspect.\x02\x03",

            "If you go around asking #4Cabout Kuper,#0C\x01",
            "something should turn up.\x02\x03",

            "Should you get a clearer picture of\x01",
            "the criminal, come back here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAA")


    ChrTalk(    #202
        0x101,
        (
            "#1015FSo once we've found the criminal,\x01",
            "go report to you?\x02\x03",

            "#1006FNo problem! Let's go see what we\x01",
            "can find out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xE, -3880, 0, 83810, 180)
    SetChrPos(0xB, -430, 0, 80990, 225)
    SetChrPos(0x14, -2450, 0, 80960, 180)
    OP_4B(0xB, 0)
    OP_4B(0x14, 0)
    OP_4B(0xE, 0)
    OP_28(0x69, 0x4, 0x2)
    OP_28(0x69, 0x4, 0x4)
    OP_28(0x69, 0x4, 0x8)
    RemoveParty(0x3, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -1300, 0, 78180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_40B4")
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -2430, 0, 79710, 0)
    Jump("loc_40D4")

    label("loc_40B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_40D4")
    RemoveParty(0x2, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -2430, 0, 79710, 0)

    label("loc_40D4")

    SetChrPos(0x101, -2160, 0, 77200, 205)
    SetChrPos(0x105, -2160, 0, 77200, 205)
    OP_30(0x0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMapFlags(0x1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_4_1E16 end

    def Function_5_413D(): pass

    label("Function_5_413D")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #203
        "\x18What would you like to ask about?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "Kuper")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_41EE")
    OP_CC(0x1, 0x0, "Sounds")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_4224")
    OP_CC(0x1, 0x0, "Anger")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_425A")
    OP_CC(0x1, 0x0, "Herio")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_425A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_4290")
    OP_CC(0x1, 0x0, "Lunch")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_42CE")
    OP_CC(0x1, 0x0, "The Bell Toll")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_42CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_430A")
    OP_CC(0x1, 0x0, "Cleaning Up")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_430A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_4341")
    OP_CC(0x1, 0x0, "Belden")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4341")

    OP_CC(0x1, 0x0, "Stop")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4389")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43AD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_43AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_43D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_43F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4419")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_443D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4461")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4485")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4485")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_448F")

    Return()

    # Function_5_413D end

    def Function_6_4490(): pass

    label("Function_6_4490")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_44BD"),
        (1, "loc_4644"),
        (2, "loc_467F"),
        (3, "loc_47C2"),
        (4, "loc_48F6"),
        (5, "loc_4FB2"),
        (6, "loc_51CC"),
        (7, "loc_528A"),
        (SWITCH_DEFAULT, "loc_52FB"),
    )


    label("loc_44BD")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4532")

    ChrTalk(    #204
        0xFE,
        (
            "When Kuper came to the hotel,\x01",
            "I was in the lobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "I dunno. He looked angry, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4641")

    label("loc_4532")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #206
        0xFE,
        (
            "When Kuper came to the hotel,\x01",
            "I was in the lobby.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_45A9")

    ChrTalk(    #207
        0xFE,
        "I dunno. He looked angry, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_45DC")

    label("loc_45A9")


    ChrTalk(    #208
        0xFE,
        "I dunno. He looked #4Cangry#0C, I guess.\x02",
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_45DC")


    ChrTalk(    #209
        0xFE,
        "I thought somethin' might happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "And then, just like I thought,\x01",
            "somethin' happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x2)

    label("loc_4641")

    Jump("loc_52FE")

    label("loc_4644")

    OP_28(0x6A, 0x1, 0x80)

    ChrTalk(    #211
        0xFE,
        "A sound?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "I didn't really hear anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_52FE")

    label("loc_467F")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_472E")

    ChrTalk(    #213
        0xFE,
        (
            "Kuper looked like he was pissed\x01",
            "off to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "I mean, it WAS right after that big\x01",
            "mess on the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "Kinda makes sense for him to be\x01",
            "angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BF")

    label("loc_472E")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #216
        0xFE,
        "Yeah, he looked pissed off to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "But, it was right after that big mess\x01",
            "on the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "It's only natural he'd be angry.\x02",
    )

    CloseMessageWindow()

    label("loc_47BF")

    Jump("loc_52FE")

    label("loc_47C2")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4851")

    ChrTalk(    #219
        0xFE,
        "So you're checkin' out Herio, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I thought he and Dels got along\x01",
            "pretty well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "I could be wrong, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48F3")

    label("loc_4851")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #222
        0xFE,
        "So you're checkin' out Herio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "He did kinda look unhappy when\x01",
            "he got back to the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "That's probably 'cause he was\x01",
            "with Kuper, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F3")

    Jump("loc_52FE")

    label("loc_48F6")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_4ACE")
    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #225
        0xFE,
        (
            "After I ate lunch on the first floor,\x01",
            "I was in the basement the whole\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "C-C'mon, why would I lie about\x01",
            "something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Still, you know what?\x01",
            "My dad's pretty unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "He feeds us normal, boring stuff,\x01",
            "then gets a special paella just for\x01",
            "himself!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACB")
    OP_A2(0xB)

    ChrTalk(    #229
        0x101,
        "#1015FHuh? Wait a sec...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #230
        0xFE,
        "What?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #231
        0xFE,
        "Wh-What is it this time?\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_4ACB")

    Jump("loc_4FAF")

    label("loc_4ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_4C03")
    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #232
        0xFE,
        "I ate lunch on the first floor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "Still, you know what?\x01",
            "My dad's pretty unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "He feeds us normal, boring stuff,\x01",
            "then gets a special paella just for\x01",
            "himself!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C00")
    OP_A2(0xB)

    ChrTalk(    #235
        0x101,
        "#1015FHuh? Wait a sec...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #236
        0xFE,
        "Wh-What's with that weird face?\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_4C00")

    Jump("loc_4FAF")

    label("loc_4C03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4D32")

    ChrTalk(    #237
        0xFE,
        "I ate lunch on the first floor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Still, you know what?\x01",
            "My dad's pretty unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "He feeds us normal, boring stuff,\x01",
            "then gets a special paella just for\x01",
            "himself!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D2F")
    OP_A2(0xB)

    ChrTalk(    #240
        0x101,
        "#1015FHuh? Wait a sec...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #241
        0xFE,
        "Wh-What's with that weird face?\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_4D2F")

    Jump("loc_4FAF")

    label("loc_4D32")

    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #242
        0xFE,
        "Yeah, we had paella for lunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "I ate on my own in the lobby.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "It's kind of suffocating to eat\x01",
            "in the same room as my dad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "Still, you know what?\x01",
            "My dad's pretty unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "He feeds us normal, boring stuff,\x01",
            "then gets a special paella just for\x01",
            "himself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        (
            "#1016FAhaha, is that so?\x02\x03",

            "Was it that different?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #248
        0xFE,
        (
            "Yeah, it was WAY better. The special\x01",
            "one's got, like, a mountain of shrimp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Guess he didn't have much of an\x01",
            "appetite, though. He left a lot behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "What a waste!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FAF")
    OP_A2(0xB)

    ChrTalk(    #251
        0x101,
        "#1015FHuh? Wait a sec...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #252
        0xFE,
        "Wh-What's with that weird face?\x02",
    )

    CloseMessageWindow()
    Call(1, 8)
    Jump("loc_4FAF")

    label("loc_4FAF")

    Jump("loc_52FE")

    label("loc_4FB2")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_50BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_504E")
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #253
        0xFE,
        (
            "I... I was in the basement, so I didn't\x01",
            "hear the bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "C-C'mon, why would I lie about\x01",
            "something like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B8")

    label("loc_504E")

    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #255
        0xFE,
        "Did the bridge bell already ring?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I was in the hotel basement, so I didn't\x01",
            "notice at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B8")

    Jump("loc_51C9")

    label("loc_50BB")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_5135")
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #257
        0xFE,
        (
            "I... I was in the basement, so I didn't\x01",
            "hear the bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "R-Really. Why would I lie?\x02",
    )

    CloseMessageWindow()
    Jump("loc_51C9")

    label("loc_5135")

    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #259
        0xFE,
        (
            "C-C'mon, why would I lie about\x01",
            "something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "I was in the hotel basement, so I didn't\x01",
            "notice at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51C9")
    Call(1, 7)

    label("loc_51C9")

    Jump("loc_52FE")

    label("loc_51CC")

    OP_28(0x6A, 0x1, 0x80)
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #261
        0xFE,
        (
            "Who cleaned up the dishes in\x01",
            "the office? Dunno. I wouldn't go\x01",
            "to that much trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "I'd been killing time in the hotel\x01",
            "basement after lunch.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5287")
    Call(1, 7)

    label("loc_5287")

    Jump("loc_52FE")

    label("loc_528A")

    OP_28(0x6A, 0x1, 0x80)

    ChrTalk(    #263
        0xFE,
        "S-So when the bell rang, I was underground.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "I was in the basement the whole time\x01",
            "after lunch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52FE")

    label("loc_52FB")

    Jump("loc_52FE")

    label("loc_52FE")

    Return()

    # Function_6_4490 end

    def Function_7_52FF(): pass

    label("Function_7_52FF")

    OP_28(0x69, 0x1, 0x2000)

    ChrTalk(    #265
        0x101,
        (
            "#1019F...\x02\x03",

            "Were you really in the basement the\x01",
            "whole time?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #266
        0xFE,
        "What?! Wh-Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1002FThere's someone who passed\x01",
            "through the basement right after\x01",
            "the bell rang.\x02\x03",

            "According to their testimony, no\x01",
            "one was here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #268
        0xFE,
        "Th-That can't be right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        "I was right here the whole time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x105,
        "#042F(So he can't establish an alibi...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #271
        0x101,
        (
            "#1002F(Just in case, we should probably\x01",
            "ask around #4Cabout Belden,#0C too)\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()
    Return()

    # Function_7_52FF end

    def Function_8_54E8(): pass

    label("Function_8_54E8")

    OP_28(0x69, 0x1, 0x1000)

    ChrTalk(    #272
        0xFE,
        "Did I say somethin' weird?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5625")

    ChrTalk(    #273
        0x101,
        (
            "#1015FNo, it's just...\x02\x03",

            "#1002F...Hey, Belden.\x02\x03",

            "You said you ate lunch on the first\x01",
            "floor, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #274
        0xFE,
        "Y-Yeah... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "What about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1015FNorman ate on the second floor.\x02\x03",

            "How did you know what Norman\x01",
            "ate when you were on the first floor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5871")

    label("loc_5625")


    ChrTalk(    #277
        0x101,
        (
            "#1015FWell, er, it's just...\x02\x03",

            "#1002F...Hey, Belden.\x02\x03",

            "You talked about the special paella,\x01",
            "right?\x02\x03",

            "How it was unfair that he only got\x01",
            "one for himself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #278
        0xFE,
        "Y-Yeah... I think I did, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "What about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1015FOkay, so here's what I don't get.\x02\x03",

            "Why would you know about it in\x01",
            "the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "Ah...haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "I... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1010FYou said you ate lunch in the first\x01",
            "floor lobby.\x02\x03",

            "Conversely, Norman ate his lunch\x01",
            "on the second floor in the office.\x02\x03",

            "#1002FYou see where I'm going with this?\x02\x03",

            "How did you know what Norman ate\x01",
            "when you were on the first floor?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5871")


    ChrTalk(    #284
        0xFE,
        "O-Oh! Uh, that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "I saw it afterwards, obvi...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #286
        0xFE,
        "...uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        "#1019F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x105,
        "#044F...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #289
        0xFE,
        "Er, sorry... My bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "Yeah, actually I heard from someone else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "I don't remember who said it, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "M-Maybe you should i-investigate that next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        "#1007F(That's so obviously suspicious.)\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_8_54E8 end

    def Function_9_59D9(): pass

    label("Function_9_59D9")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A06"),
        (1, "loc_5A98"),
        (2, "loc_5AE3"),
        (3, "loc_5BA8"),
        (4, "loc_628D"),
        (5, "loc_6376"),
        (6, "loc_66E8"),
        (7, "loc_6776"),
        (SWITCH_DEFAULT, "loc_68BA"),
    )


    label("loc_5A06")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #294
        0xA,
        (
            "Mister Kuper is a guest who comes\x01",
            "here only on very rare occasions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xA,
        (
            "Mostly, we have his patronage for\x01",
            "work-related gatherings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68BD")

    label("loc_5A98")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #296
        0xA,
        "A sound, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xA,
        "Unfortunately, I heard no such thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_68BD")

    label("loc_5AE3")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5B54")

    ChrTalk(    #298
        0xA,
        "Mister Kuper seemed generally normal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "He didn't appear to be particularly\x01",
            "angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BA5")

    label("loc_5B54")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #300
        0xA,
        "I fear I cannot agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xA,
        "Mister Kuper seemed generally normal.\x02",
    )

    CloseMessageWindow()

    label("loc_5BA5")

    Jump("loc_68BD")

    label("loc_5BA8")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_5C7A")

    ChrTalk(    #302
        0xA,
        (
            "I apologize for remaining silent on\x01",
            "something I should have mentioned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xA,
        (
            "However, I'm certain Herio could not\x01",
            "be the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xA,
        (
            "I couldn't imagine him committing any\x01",
            "such crime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_628A")

    label("loc_5C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_6158")
    OP_28(0x69, 0x1, 0x10)
    OP_A2(0xE)
    OP_A2(0xF)

    ChrTalk(    #305
        0xA,
        "Y-You still doubt Herio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "Herio is a most loyal man. He would\x01",
            "never commit such a criminal act!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xA,
        "It's impossible for him to be the criminal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        (
            "#1002F???\x02\x03",

            "Wh-What is it? What's on your mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x17, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5DF4")
    OP_4A(0x15, 0)

    ChrTalk(    #309
        0x15,
        (
            "#057FIf you're hiding something,\x01",
            "you should spit it out.\x02\x03",

            "Trying to hide things only bites\x01",
            "you in the ass most of the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E83")

    label("loc_5DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5E83")
    OP_4A(0x16, 0)

    ChrTalk(    #310
        0x16,
        (
            "#027FIf you're hiding something, you\x01",
            "should just come out and say it.\x02\x03",

            "Trying to hide things will only\x01",
            "lead to bigger trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E83")


    ChrTalk(    #311
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xA,
        "I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1002FFeel like talking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xA,
        "Yes, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xA,
        "I saw him. I saw Herio on the second floor.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5F30")

    ChrTalk(    #316
        0x15,
        "#057F...When was that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x15, 400)
    Jump("loc_5F5E")

    label("loc_5F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5F5E")

    ChrTalk(    #317
        0x16,
        "#022F...And when was that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x16, 400)

    label("loc_5F5E")

    Sleep(400)

    ChrTalk(    #318
        0xA,
        "Right #4Cafter lunch#0C.\x02",
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #319
        0xA,
        "Herio went out with Norman, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xA,
        (
            "However, shortly after that, Herio came\x01",
            "back and ran up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#1002FWhoa, that's kinda important to know.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_60A5")
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #322
        0x15,
        (
            "#050FEstelle, you go after this lead.\x02\x03",

            "We're gonna check around here\x01",
            "for a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x15, 400)
    Jump("loc_6117")

    label("loc_60A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6117")
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(    #323
        0x16,
        (
            "#022FEstelle, I want you to pursue this lead.\x02\x03",

            "We'll look around here for a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 400)

    label("loc_6117")


    ChrTalk(    #324
        0x101,
        "#1002FGot it.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6143")
    OP_4B(0x15, 0)
    TurnDirection(0x15, 0xA, 0)
    Jump("loc_6155")

    label("loc_6143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6155")
    OP_4B(0x16, 0)
    TurnDirection(0x16, 0xA, 0)

    label("loc_6155")

    Jump("loc_628A")

    label("loc_6158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_620C")
    OP_28(0x6A, 0x1, 0x8)

    ChrTalk(    #325
        0xA,
        "You doubt even Herio?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xA,
        (
            "He isn't the kind of person to resort\x01",
            "to violence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xA,
        (
            "Herio is a most loyal man. He would\x01",
            "never commit such a criminal act!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_628A")

    label("loc_620C")


    ChrTalk(    #328
        0xA,
        (
            "Herio is a most loyal man. He would\x01",
            "never commit such a criminal act!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xA,
        "It's impossible for him to be the criminal...\x02",
    )

    CloseMessageWindow()

    label("loc_628A")

    Jump("loc_68BD")

    label("loc_628D")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_630D")

    ChrTalk(    #330
        0xA,
        "After lunch, Norman and Herio both left.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "Herio later came back and went up to\x01",
            "the second floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6373")

    label("loc_630D")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #332
        0xA,
        "Lunch was ordered from the Lavantar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xA,
        (
            "Everyone had their lunch\x01",
            "where they saw fit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6373")

    Jump("loc_68BD")

    label("loc_6376")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_6404")

    ChrTalk(    #334
        0xA,
        (
            "When the noon bell rang,\x01",
            "I was tidying the utensils.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xA,
        (
            "Someone was kind enough to\x01",
            "clean the plates in the office.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66E5")

    label("loc_6404")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_28(0x69, 0x1, 0x800)

    ChrTalk(    #336
        0xA,
        "The noon bridge bell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        (
            "Yes, at that time I was preparing\x01",
            "the guest rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xA,
        (
            "Once that was finished, I next\x01",
            "organized the utensils.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xA,
        (
            "Someone had cleaned the plates\x01",
            "in the office, so I was able to finish\x01",
            "work quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #340
        0x105,
        "#044FThe office plates were cleaned...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1004FSo that means...\x02\x03",

            "There was someone who went into\x01",
            "the office after lunch?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #342
        0xA,
        "Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xA,
        (
            "While I was preparing the guest rooms,\x01",
            "they #4Ccleaned up#0C, it seems...\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #344
        0xA,
        "The plates were stacked at the front.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xA,
        (
            "Of course, exactly which kind guest\x01",
            "it was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xA,
        "I couldn't say, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1007FAww, too bad.\x02\x03",

            "Guess we'll have to ask\x01",
            "around ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E5")

    Jump("loc_68BD")

    label("loc_66E8")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #348
        0xA,
        (
            "Exactly who cleaned up, unfortunately,\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xA,
        (
            "While I was preparing the guest rooms,\x01",
            "someone must have cleaned up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68BD")

    label("loc_6776")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6820")

    ChrTalk(    #350
        0xA,
        "Young Belden...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xA,
        (
            "I am afraid I didn't see him\x01",
            "around when the bell rang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        (
            "When I finished cleaning the\x01",
            "utensils, he was in the lobby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B7")

    label("loc_6820")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #353
        0xA,
        "Young Belden...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xA,
        (
            "I'm afraid I didn't see him\x01",
            "around when the bell rang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xA,
        (
            "I was preparing the guest rooms\x01",
            "at the time, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B7")

    Jump("loc_68BD")

    label("loc_68BA")

    Jump("loc_68BD")

    label("loc_68BD")

    Return()

    # Function_9_59D9 end

    def Function_10_68BE(): pass

    label("Function_10_68BE")

    TalkBegin(0xFE)
    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_68EE"),
        (1, "loc_6AD7"),
        (2, "loc_6D0E"),
        (3, "loc_6F9C"),
        (4, "loc_70FF"),
        (5, "loc_7187"),
        (6, "loc_7377"),
        (7, "loc_73FA"),
        (SWITCH_DEFAULT, "loc_7456"),
    )


    label("loc_68EE")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6965")

    ChrTalk(    #356
        0xFE,
        (
            "If we were fightin', someone\x01",
            "would have heard a sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        "No one said anything, did they?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AD4")

    label("loc_6965")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #358
        0xFE,
        (
            "I'll say it as many times as you like!\x01",
            "I only found Dels.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6A1C")

    ChrTalk(    #359
        0xFE,
        (
            "If we'd been fightin', someone would've\x01",
            "heard a sound. But no one said anything,\x01",
            "did they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A87")

    label("loc_6A1C")


    ChrTalk(    #360
        0xFE,
        (
            "If we'd been fightin', someone would've\x01",
            "heard a #4Csound#0C, but no one said\x01",
            "anything, did they?\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_6A87")


    ChrTalk(    #361
        0xFE,
        (
            "Of course they didn't, because I was\x01",
            "politely seated on the sofa.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x1)

    label("loc_6AD4")

    Jump("loc_7459")

    label("loc_6AD7")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6B70")

    ChrTalk(    #362
        0xFE,
        (
            "I sure didn't hear any big sound when\x01",
            "I was in the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "You positive the person who said that\x01",
            "doesn't have bad hearing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D0B")

    label("loc_6B70")


    ChrTalk(    #364
        0xFE,
        (
            "If I'd fought with Dels, someone would\x01",
            "have heard somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_6D0B")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #365
        0x101,
        (
            "#1015FWe actually have someone who\x01",
            "testified to hearing a loud sound.\x02\x03",

            "He apparently heard the sound of\x01",
            "something colliding with something\x01",
            "else from around the balcony area.\x02\x03",

            "#1002FDo you have any idea what it could\x01",
            "have been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "Something colliding with something\x01",
            "else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        "Nope. I didn't hear any sound like that.\x02",
    )

    CloseMessageWindow()

    label("loc_6D0B")

    Jump("loc_7459")

    label("loc_6D0E")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6DAA")

    ChrTalk(    #368
        0xFE,
        "I wasn't angry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "I came to apologize as a representative\x01",
            "of our camp, if you must know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "I wouldn't come here all angry!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F99")

    label("loc_6DAA")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #371
        0xFE,
        "I was angry? Pfft! That's crazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "If you're gonna say that, Herio's\x01",
            "attitude was way worse than mine,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        (
            "The moment he saw me, he made\x01",
            "this real nasty face.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_6EB7")

    ChrTalk(    #374
        0xFE,
        (
            "Try asking around about Herio.\x01",
            "I bet you'll turn up some dirt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F06")

    label("loc_6EB7")


    ChrTalk(    #375
        0xFE,
        (
            "Try asking around #4Cabout Herio#0C.\x01",
            "I bet you'll turn up some dirt.\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_6F06")


    ChrTalk(    #376
        0xFE,
        (
            "Him and Dels are rivals competing\x01",
            "to be the No. 2 in Norman's camp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "I'm sure they couldn't come to\x01",
            "terms and ended up in a tussle.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x8)

    label("loc_6F99")

    Jump("loc_7459")

    label("loc_6F9C")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_703F")

    ChrTalk(    #378
        0xFE,
        (
            "Him and Dels are rivals competing\x01",
            "to be the No. 2 in Norman's camp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "I'm sure they couldn't come to\x01",
            "terms and ended up in a tussle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FC")

    label("loc_703F")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #380
        0xFE,
        "Herio's got motive too, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "Him and Dels are rivals competing\x01",
            "to be No. 2 in Norman's camp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "I'm sure they couldn't come to terms\x01",
            "and ended up in a tussle.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6A, 0x1, 0x2000)

    label("loc_70FC")

    Jump("loc_7459")

    label("loc_70FF")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #383
        0xFE,
        "So they ordered from the Lavantar?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "That sure is nice. Maybe I'll try asking\x01",
            "Portos if we can do something like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7459")

    label("loc_7187")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #385
        0xFE,
        "The bridge toll?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "Yeah, I was running across the\x01",
            "bridge in a real hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "I met Norman right about the same\x01",
            "time by the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7374")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733B")
    OP_28(0x69, 0x1, 0x100)

    ChrTalk(    #388
        0x101,
        (
            "#1019FHmmmm. So then...\x02\x03",

            "Kuper and the balcony sound are\x01",
            "unrelated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x105,
        (
            "#047FAccording to the testimony we got,\x01",
            "the sound happened right after the\x01",
            "bell stopped ringing, so...\x02\x03",

            "#042FThat would line up with what we've\x01",
            "heard from Kuper himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7374")

    label("loc_733B")


    ChrTalk(    #390
        0x101,
        (
            "#1002FI see...\x02\x03",

            "That does match Norman's testimony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7374")

    Jump("loc_7459")

    label("loc_7377")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #391
        0xFE,
        (
            "You're looking for the person\x01",
            "who cleaned up the plates?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "Look, who cares?! Just hurry up and\x01",
            "prove me innocent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7459")

    label("loc_73FA")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #393
        0xFE,
        "Where was Belden when the bell rang?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        "How the hell am I supposed to know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7459")

    label("loc_7456")

    Jump("loc_7459")

    label("loc_7459")

    TalkEnd(0xFE)
    Return()

    # Function_10_68BE end

    def Function_11_745D(): pass

    label("Function_11_745D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_74DC")

    ChrTalk(    #395
        0xFE,
        (
            "#030FI believe we're almost done here.\x02\x03",

            "Let's hurry and solve this so we\x01",
            "can enjoy a cup in celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D86")

    label("loc_74DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_7655")
    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_758A")

    ChrTalk(    #396
        0xFE,
        (
            "#035FI was raised in the city, so I fear\x01",
            "I'm dreadful with standing around.\x02\x03",

            "As they say! The more beautiful\x01",
            "the flower, the easier it wilts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7652")

    label("loc_758A")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #397
        0xFE,
        (
            "#034FPhew! I'm afraid my power is ebbing.\x02\x03",

            "I was raised in the city, so I fear\x01",
            "I'm dreadful with standing around.\x02\x03",

            "#037FAs they say! The more beautiful\x01",
            "the flower, the easier it wilts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7652")

    Jump("loc_7D86")

    label("loc_7655")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_77B5")
    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7716")

    ChrTalk(    #398
        0xFE,
        (
            "#035FI'd previously read about the bell\x01",
            "in a guide book.\x02\x03",

            "It's a charming feature, but it would\x01",
            "have been ever more luxurious were\x01",
            "it a flute instead of a bell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77B2")

    label("loc_7716")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #399
        0xFE,
        (
            "#030FThe bell? You mean the bell in the\x01",
            "grand bridge?\x02\x03",

            "I remember reading about that\x01",
            "before...somewhere...\x02\x03",

            "Ah, yes! It was in a guide book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B2")

    Jump("loc_7D86")

    label("loc_77B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_796E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7846")

    ChrTalk(    #400
        0xFE,
        (
            "#031FI thought it was odd, but it was\x01",
            "precisely as I saw.\x02\x03",

            "I am truly a sinful soul to read\x01",
            "the hearts of men so well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_796B")

    label("loc_7846")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_78C2")

    ChrTalk(    #401
        0xFE,
        (
            "#030FI asked about today's lunch menu.\x02\x03",

            "The problem was certainly the\x01",
            "appetizer, in my humble opinion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_796B")

    label("loc_78C2")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #402
        0xFE,
        (
            "#030FI asked about today's lunch menu.\x02\x03",

            "#035FThe problem was certainly the\x01",
            "appetizer, in my humble opinion.\x02\x03",

            "I wish they'd served a more\x01",
            "thoughtful dish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_796B")

    Jump("loc_7D86")

    label("loc_796E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_79FD")

    ChrTalk(    #403
        0xFE,
        (
            "#032FThe people at the front are acting\x01",
            "most peculiarly.\x02\x03",

            "If you push them with questions,\x01",
            "you might uncover something new.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D86")

    label("loc_79FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_7C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7AB8")

    ChrTalk(    #404
        0xFE,
        (
            "#034F*sigh* Such cruelty.\x02\x03",

            "Agate hasn't paid me any attention at\x01",
            "all! Not a flutter of those heavy lashes\x01",
            "has gone my way.\x02\x03",

            "#032FPerhaps I will blow in his ear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B6A")

    label("loc_7AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7B6A")

    ChrTalk(    #405
        0xFE,
        (
            "#034F*sigh* Such cruelty.\x02\x03",

            "Scherazard hasn't paid me any\x01",
            "attention at all. Not once has her\x01",
            "whip even twitched in my direction.\x02\x03",

            "#032FPerhaps I will blow in her ear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7B7A")
    Jump("loc_7BFD")

    label("loc_7B7A")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #406
        0x101,
        (
            "#1015FWell, I won't stop you.\x02\x03",

            "#1007FJust know that we're gonna go\x01",
            "from an assault case to a murder\x01",
            "case if you do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFD")

    Jump("loc_7D86")

    label("loc_7C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7CB6")

    ChrTalk(    #407
        0xFE,
        (
            "#030FThe evening view here is probably\x01",
            "quite breathtaking.\x02\x03",

            "If I had the time, I would share a\x01",
            "drink with the night sky and savor\x01",
            "the embrace of its starry folds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D86")

    label("loc_7CB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7D21")

    ChrTalk(    #408
        0xFE,
        (
            "#031FHeh! My graceful conversational skills\x01",
            "finally have their time in the spotlight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D86")

    label("loc_7D21")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #409
        0xFE,
        (
            "#031FHeh! My graceful conversational skills\x01",
            "finally have their time in the spotlight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D86")

    TalkEnd(0xFE)
    Return()

    # Function_11_745D end

    def Function_12_7D8A(): pass

    label("Function_12_7D8A")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7DB7"),
        (1, "loc_7F1D"),
        (2, "loc_7FCC"),
        (3, "loc_8065"),
        (4, "loc_81E4"),
        (5, "loc_8697"),
        (6, "loc_8A48"),
        (7, "loc_8EB7"),
        (SWITCH_DEFAULT, "loc_8F8E"),
    )


    label("loc_7DB7")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7E4F")

    ChrTalk(    #410
        0xFE,
        (
            "Kuper was standing next to Dels,\x01",
            "who was lying on the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xFE,
        (
            "He had a very surprised expression\x01",
            "on his face, I recall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1A")

    label("loc_7E4F")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #412
        0xFE,
        (
            "Kuper was standing next to Dels,\x01",
            "who was lying on the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xFE,
        (
            "He looked at me, and seemed very\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "He wasn't excited or worked up,\x01",
            "but he did appear tremendously\x01",
            "shocked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F1A")

    Jump("loc_8F91")

    label("loc_7F1D")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #415
        0xFE,
        (
            "As Kuper said, I didn't hear any\x01",
            "loud noise, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        (
            "I was in the lobby at the time, but\x01",
            "if grown men were fighting, I'm sure\x01",
            "I would have heard something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F91")

    label("loc_7FCC")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #417
        0xFE,
        (
            "He didn't seem particularly angry\x01",
            "when I met him at the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "Well, perhaps something happened\x01",
            "while he was being led to the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F91")

    label("loc_8065")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_8116")

    ChrTalk(    #419
        0xFE,
        (
            "The idea of a scuffle over who will\x01",
            "be my right-hand man is nothing\x01",
            "short of idiotic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "I trust that you wouldn't believe\x01",
            "such a rumor, of course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81E1")

    label("loc_8116")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #421
        0xFE,
        (
            "It's unbelievable that you would\x01",
            "suspect Herio...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "In the first place, you're suggesting\x01",
            "that he would hurt his coworker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "And what could possibly motivate\x01",
            "him to do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81E1")

    Jump("loc_8F91")

    label("loc_81E4")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_82B4")

    ChrTalk(    #424
        0xFE,
        (
            "After lunch, Herio and I went to have\x01",
            "a look at the place where I'll be giving\x01",
            "a speech later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "Herio had some other business to\x01",
            "attend to first and met up with me at\x01",
            "the site.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8694")

    label("loc_82B4")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #426
        0xFE,
        (
            "Yes, we ordered lunch today from the\x01",
            "Lavantar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "I don't want my campaigners getting sick\x01",
            "of eating the same food again and again,\x01",
            "so I thought we'd try something different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1011FWow. It's nice of you to do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x105,
        (
            "#040FThat's as much a part of politics\x01",
            "as the campaign itself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #430
        0xFE,
        "Haha, indeed, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "I'll admit, my nerves have been on edge for\x01",
            "some time now. It hasn't been easy to keep\x01",
            "my eyes on everything day in and day out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x105,
        "#045FI'm...sorry to hear that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1007FYikes... That does sound pretty rough.\x02\x03",

            "#1002FPutting that aside, sir...\x02\x03",

            "What did you do after lunch?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #434
        0xFE,
        (
            "After lunch, Herio and I immediately\x01",
            "went to examine the place my speech\x01",
            "is to be held at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "Herio had some other business to\x01",
            "attend to first and met up with me at\x01",
            "the site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x101,
        (
            "#1000FSo you left right after lunch and\x01",
            "met up with Herio outside?\x02\x03",

            "All right, that's all I need to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        "I'm happy to have helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        "Keep up the good work, you two.\x02",
    )

    CloseMessageWindow()

    label("loc_8694")

    Jump("loc_8F91")

    label("loc_8697")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_871F")

    ChrTalk(    #439
        0xFE,
        "When did the bridge bell ring?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        (
            "It went off when Herio and I were checking\x01",
            "out the speech site together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A45")

    label("loc_871F")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #441
        0xFE,
        "When did the bridge bell ring?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "It went off when Herio and I were checking\x01",
            "out the speech site together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x101,
        "#1002FHerio was there, too?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #444
        0xFE,
        "Yes, he was already there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "Just as the bell was ringing,\x01",
            "Kuper showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "I'd then asked Herio to show\x01",
            "him to the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x101,
        "#1015FI see, then it's sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A45")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #448
        0x105,
        (
            "#043FSo, then, Estelle...\x02\x03",

            "There's no connection between the\x01",
            "sound Murray heard and Herio.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #449
        0x101,
        (
            "#1015FYeah, not just Herio but Kuper\x01",
            "seems in the clear too.\x02\x03",

            "The sound Murray heard was just\x01",
            "after the bell finished ringing, but...\x02\x03",

            "Both men can prove they were with\x01",
            "Norman at the time.\x02\x03",

            "#1002FIn other words, whoever made that\x01",
            "sound was neither Herio nor Kuper.\x02\x03",

            "This virtually eliminates any chance\x01",
            "of them being the criminal.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x400)

    label("loc_8A45")

    Jump("loc_8F91")

    label("loc_8A48")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D12")
    OP_28(0x6A, 0x1, 0x4)

    ChrTalk(    #450
        0xFE,
        "Who could have done it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "All I know is that they were\x01",
            "cleaned while I was away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x101,
        "#1015FSo...you don't know either, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #453
        0xFE,
        "I'm afraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0xFE,
        "I don't know who it was, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        (
            "I worry that I may have left them\x01",
            "a terrible impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x101,
        "#1011FPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x105,
        "#043FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #458
        0xFE,
        (
            "In truth, I haven't had much of an\x01",
            "appetite lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "I left quite a lot of the paella I got\x01",
            "for lunch uneaten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        (
            "I'd requested that Ernest get me\x01",
            "one of the special paellas in secret\x01",
            "yet left it virtually untouched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xFE,
        (
            "It's embarrassing to think back on\x01",
            "how wasteful that was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x101,
        (
            "#1007FI see...\x02\x03",

            "It must be really stressful to be\x01",
            "running in an election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8D12")


    ChrTalk(    #463
        0xFE,
        (
            "Everything was cleaned while I was\x01",
            "out, as far as I'm aware.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "It's embarrassing to think back on\x01",
            "how wasteful I was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "I'd requested that Ernest get me\x01",
            "one of the special paellas in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xFE,
        (
            "Ultimately, I just couldn't find my\x01",
            "appetite and left it virtually untouched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "I'm sorry, but could you please keep\x01",
            "that to yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        (
            "I don't want people worried that I may\x01",
            "be sick or in poor health.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EB4")

    Jump("loc_8F91")

    label("loc_8EB7")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #469
        0xFE,
        (
            "My son's location when the bell\x01",
            "rang could pose a problem, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        (
            "If you have real cause for suspicion,\x01",
            "you needn't hesitate on my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "You're welcome to confront Belden\x01",
            "and question him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F91")

    label("loc_8F8E")

    Jump("loc_8F91")

    label("loc_8F91")

    Return()

    # Function_12_7D8A end

    def Function_13_8F92(): pass

    label("Function_13_8F92")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8FBF"),
        (1, "loc_90C9"),
        (2, "loc_91E7"),
        (3, "loc_922A"),
        (4, "loc_9376"),
        (5, "loc_93BE"),
        (6, "loc_9526"),
        (7, "loc_96A1"),
        (SWITCH_DEFAULT, "loc_978D"),
    )


    label("loc_8FBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_9033")

    ChrTalk(    #472
        0xFE,
        (
            "*sigh* It sure would've been handy\x01",
            "if I'd seen the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        "Owww... My head still hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_90C6")

    label("loc_9033")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #474
        0xFE,
        (
            "I lost consciousness immediately,\x01",
            "so I didn't see who hit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "Even catching a glance would've\x01",
            "been better than nothing at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90C6")

    Jump("loc_9790")

    label("loc_90C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_9151")

    ChrTalk(    #476
        0xFE,
        (
            "If there was some sound,\x01",
            "it would've been when I was hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "Heard a hell of a bang IN my head,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91E4")

    label("loc_9151")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #478
        0xFE,
        "A sound, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "That would probably be the sound\x01",
            "of me getting hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "Heard a hell of a bang IN my head,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91E4")

    Jump("loc_9790")

    label("loc_91E7")


    ChrTalk(    #481
        0xFE,
        "Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xFE,
        "I'm not sure I can really help with that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9790")

    label("loc_922A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_92A5")

    ChrTalk(    #483
        0xFE,
        (
            "I'd be willing to legally testify\x01",
            "that Herio's not the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xFE,
        "The guy has, like, zero motive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9373")

    label("loc_92A5")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #485
        0xFE,
        (
            "There's no way Herio did it.\x01",
            "I'd testify to it myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0xFE,
        (
            "There's no bad blood between us\x01",
            "whatsoever. We even work together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        (
            "Owww... S-Sorry, I got excited and\x01",
            "it made my head hurt...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9373")

    Jump("loc_9790")

    label("loc_9376")


    ChrTalk(    #488
        0xFE,
        "Yeah, we ordered food from the Lavantar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0xFE,
        "Man, it was GOOD!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9790")

    label("loc_93BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_945A")

    ChrTalk(    #490
        0xFE,
        (
            "Just before I lost consciousness,\x01",
            "I think I heard the sound of a bell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xFE,
        (
            "My memory's a bit unclear,\x01",
            "so I can't say for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9523")

    label("loc_945A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #492
        0xFE,
        "The sound of the bridge bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "Now that you mention it, I do think\x01",
            "I heard that before I got hit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "Hmm, I'm sorry. My head feels like\x01",
            "a wreck right now. Nothing's too clear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9523")

    Jump("loc_9790")

    label("loc_9526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_95A8")

    ChrTalk(    #495
        0xFE,
        (
            "I was in the office, so if someone had\x01",
            "cleaned up, normally I'd have noticed,\x01",
            "wouldn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        "That's weird.\x02",
    )

    CloseMessageWindow()
    Jump("loc_969E")

    label("loc_95A8")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #497
        0xFE,
        "Now that you mention it, who DID clean up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        "I'm sorry... I don't remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x101,
        (
            "#1002FBut you were in the office, weren't you?\x02\x03",

            "You'd normally notice if someone came\x01",
            "to clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0xFE,
        "You're right, I would. Even I think it's odd.\x02",
    )

    CloseMessageWindow()

    label("loc_969E")

    Jump("loc_9790")

    label("loc_96A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_972C")

    ChrTalk(    #501
        0xFE,
        "Where was Belden when the bell rang?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xFE,
        "No point in asking me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        (
            "I don't even remember if I heard the\x01",
            "bell ring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_978A")

    label("loc_972C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #504
        0xFE,
        "Where was Belden when the bell rang?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        "I don't know, but...is he a suspect?\x02",
    )

    CloseMessageWindow()

    label("loc_978A")

    Jump("loc_9790")

    label("loc_978D")

    Jump("loc_9790")

    label("loc_9790")

    Return()

    # Function_13_8F92 end

    def Function_14_9791(): pass

    label("Function_14_9791")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B06")
    EventBegin(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8B(0x101, 0x164E, 0x1E, 0x190)

    ChrTalk(    #506
        0x101,
        "#1011FOh!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(2870, 0, 2140, 0)
    SetChrPos(0x101, 560, 0, 2430, 122)
    SetChrPos(0x105, -370, 0, 2740, 122)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_982D")
    OP_4A(0x15, 0)
    OP_43(0x15, 0x1, 0x1, 0x1B)
    Jump("loc_983F")

    label("loc_982D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_983F")
    OP_4A(0x16, 0)
    OP_43(0x16, 0x1, 0x1, 0x1B)

    label("loc_983F")

    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9870")

    def lambda_9851():

        label("loc_9851")

        TurnDirection(0x101, 0x15, 400)
        OP_48()
        Jump("loc_9851")

    QueueWorkItem2(0x101, 2, lambda_9851)

    def lambda_9862():

        label("loc_9862")

        TurnDirection(0x105, 0x15, 400)
        OP_48()
        Jump("loc_9862")

    QueueWorkItem2(0x105, 2, lambda_9862)
    Jump("loc_9899")

    label("loc_9870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9899")

    def lambda_987D():

        label("loc_987D")

        TurnDirection(0x101, 0x16, 400)
        OP_48()
        Jump("loc_987D")

    QueueWorkItem2(0x101, 2, lambda_987D)

    def lambda_988E():

        label("loc_988E")

        TurnDirection(0x105, 0x16, 400)
        OP_48()
        Jump("loc_988E")

    QueueWorkItem2(0x105, 2, lambda_988E)

    label("loc_9899")

    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_98AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_98AA)
    OP_4A(0x17, 0)
    OP_43(0x17, 0x1, 0x1, 0x1C)

    def lambda_98C7():
        OP_6D(560, 0, 2430, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_98C7)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #507
        0x101,
        (
            "#1000FAre you done questioning\x01",
            "in the office?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9959")

    ChrTalk(    #508
        0x15,
        (
            "#050FYeah, we're done.\x02\x03",

            "How's it goin' on your end?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9990")

    label("loc_9959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9990")

    ChrTalk(    #509
        0x16,
        (
            "#020FYes, we're done here.\x02\x03",

            "How about you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9990")


    ChrTalk(    #510
        0x101,
        (
            "#1015FIt's going okay, I guess.\x02\x03",

            "#1006FI'm still checking out stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9A04")

    ChrTalk(    #511
        0x15,
        "#050FJust don't slack off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A39")

    label("loc_9A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9A39")

    ChrTalk(    #512
        0x16,
        "#020FKeep it up, and don't get careless.\x02",
    )

    CloseMessageWindow()

    label("loc_9A39")


    ChrTalk(    #513
        0x101,
        "#1000FLeave it to me!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9A65")
    OP_43(0x15, 0x1, 0x1, 0x1D)
    Jump("loc_9A73")

    label("loc_9A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9A73")
    OP_43(0x16, 0x1, 0x1, 0x1D)

    label("loc_9A73")

    Sleep(400)
    OP_43(0x17, 0x1, 0x1, 0x1E)
    WaitChrThread(0x17, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9AA3")
    SetChrPos(0x15, -3320, 0, 9510, 45)
    OP_4B(0x15, 0)
    Jump("loc_9ABF")

    label("loc_9AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9ABF")
    SetChrPos(0x16, -3320, 0, 9510, 45)
    OP_4B(0x16, 0)

    label("loc_9ABF")

    SetChrPos(0x17, -2620, 0, 8220, 0)
    OP_4B(0x17, 0)
    OP_28(0x6A, 0x1, 0x10)
    SetChrPos(0x14, -7880, 0, 83450, 0)
    SetChrPos(0xE, -3740, 0, 78670, 0)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x2)
    EventEnd(0x0)

    label("loc_9B06")

    Return()

    # Function_14_9791 end

    def Function_15_9B07(): pass

    label("Function_15_9B07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C44")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9B5A")

    ChrTalk(    #514
        0x101,
        "#1007FWe still can't leave.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BA8")

    label("loc_9B5A")

    OP_A2(0x9)

    ChrTalk(    #515
        0x101,
        (
            "#1015FWait, this way's the exit.\x02\x03",

            "I'd better get back to questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BA8")

    Jump("loc_9C29")

    label("loc_9BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9BDE")

    ChrTalk(    #516
        0x105,
        "#042FWe can't go anywhere else yet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C29")

    label("loc_9BDE")

    OP_A2(0x9)

    ChrTalk(    #517
        0x105,
        (
            "#042FThis is the exit.\x02\x03",

            "Right now we'd best return to questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C29")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_9C44")

    Return()

    # Function_15_9B07 end

    def Function_16_9C45(): pass

    label("Function_16_9C45")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xFE, 0x0, 0)
    OP_4A(0xFE, 0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",         # 0
            "Report\x01",       # 1
            "Give Up\x01",      # 2
            "Stop\x01",         # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9CCD"),
        (1, "loc_9D0C"),
        (2, "loc_9D36"),
        (SWITCH_DEFAULT, "loc_9FD6"),
    )


    label("loc_9CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9CDB")
    Call(1, 17)
    Jump("loc_9CE6")

    label("loc_9CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9CE6")
    Call(1, 18)

    label("loc_9CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_9CFB")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_9D02")

    label("loc_9CFB")

    OP_8C(0xFE, 0, 0)

    label("loc_9D02")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_9FFC")

    label("loc_9D0C")

    Call(1, 19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_9D25")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_9D2C")

    label("loc_9D25")

    OP_8C(0xFE, 0, 0)

    label("loc_9D2C")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_9FFC")

    label("loc_9D36")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #518
        "\x07\x05Will you give up?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Give Up\x01",               # 0
            "Try a Bit Longer\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DEF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_9DE0")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_9DE7")

    label("loc_9DE0")

    OP_8C(0xFE, 0, 0)

    label("loc_9DE7")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    label("loc_9DEF")

    EventBegin(0x0)
    TurnDirection(0x17, 0x0, 0)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9E9C")

    ChrTalk(    #519
        0x15,
        (
            "#052FYou're throwin' in the towel?\x02\x03",

            "#053FFine, whatever you want.\x02\x03",

            "#050FI'll finish the investigation. You wait\x01",
            "outside until things're settled.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F5C")

    label("loc_9E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9F5C")

    ChrTalk(    #520
        0x16,
        (
            "#023FYou're giving up?\x02\x03",

            "#026FWell, if you're not confident you\x01",
            "can solve it, that's fair, I guess.\x02\x03",

            "#022FI'll continue the investigation. You wait\x01",
            "outside until things're settled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F5C")

    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #521
        "Quest #CR#[Election Office Assault] #CW#failed...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x69, 0x4, 0x80)
    OP_28(0x69, 0x4, 0x40)
    OP_28(0x69, 0x1, 0x4000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9FFC")

    label("loc_9FD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_9FEB")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_9FF2")

    label("loc_9FEB")

    OP_8C(0xFE, 0, 0)

    label("loc_9FF2")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_9FFC")

    label("loc_9FFC")

    Return()

    # Function_16_9C45 end

    def Function_17_9FFD(): pass

    label("Function_17_9FFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_A078")

    ChrTalk(    #522
        0xFE,
        (
            "#050FLooks like we're not far off from\x01",
            "pointing out the criminal.\x02\x03",

            "Once you got your mark, come report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50B")

    label("loc_A078")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_A139")

    ChrTalk(    #523
        0xFE,
        (
            "#050FThe more digging you do, the\x01",
            "more you're sure to find somethin'\x01",
            "worthwhile.\x02\x03",

            "If you're stuck, you might wanna\x01",
            "go over everything again.\x02\x03",

            "If you give up, that's the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50B")

    label("loc_A139")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_A1A8")

    ChrTalk(    #524
        0xFE,
        (
            "#050FThe sound of a bell?\x01",
            "Sounds like it could be a clue.\x02\x03",

            "I don't mind. Do it as you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50B")

    label("loc_A1A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_A20D")

    ChrTalk(    #525
        0xFE,
        (
            "#050FGo ahead and pursue that new info.\x02\x03",

            "I'm gonna stick here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A251")

    label("loc_A20D")


    ChrTalk(    #526
        0xFE,
        (
            "#050FGot somethin'?\x02\x03",

            "Make sure you stick to it. Don't give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A251")

    Jump("loc_A50B")

    label("loc_A254")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A32B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A2BD")

    ChrTalk(    #527
        0xFE,
        (
            "#050FGo ahead and pursue that new info.\x02\x03",

            "I'm gonna stick here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A328")

    label("loc_A2BD")


    ChrTalk(    #528
        0xFE,
        (
            "#050FSeems like we've found a new lead\x01",
            "to investigate.\x02\x03",

            "I'd like some reliable testimony here,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A328")

    Jump("loc_A50B")

    label("loc_A32B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_A399")

    ChrTalk(    #529
        0xFE,
        (
            "#050FThe suspect remains unclear.\x02\x03",

            "Think it's about time we widened\x01",
            "our investigative net.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50B")

    label("loc_A399")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_A426")

    ChrTalk(    #530
        0xFE,
        (
            "#050FWe're stuck talkin' to the suspect,\x01",
            "but nothin's real clear still.\x02\x03",

            "Don't get fooled by some obviously\x01",
            "BS testimony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50B")

    label("loc_A426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A4B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_A468")

    ChrTalk(    #531
        0xFE,
        "#050F...If you get it, get goin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4AE")

    label("loc_A468")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #532
        0xFE,
        (
            "#050FFound some new material?\x02\x03",

            "If so, follow up on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4AE")

    Jump("loc_A50B")

    label("loc_A4B1")


    ChrTalk(    #533
        0xFE,
        (
            "#050FFirst, ask about the suspect.\x02\x03",

            "If you find some new material,\x01",
            "follow that next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50B")

    Return()

    # Function_17_9FFD end

    def Function_18_A50C(): pass

    label("Function_18_A50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_A58A")

    ChrTalk(    #534
        0xFE,
        (
            "#020FLooks like we're not far off from\x01",
            "the resolution.\x02\x03",

            "Once you've fixed on a suspect,\x01",
            "come report to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA89")

    label("loc_A58A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_A64B")

    ChrTalk(    #535
        0xFE,
        (
            "#022FThe more digging you do, the\x01",
            "more you're sure to find somethin'\x01",
            "worthwhile.\x02\x03",

            "If you're stuck, you might wanna\x01",
            "go over everything again.\x02\x03",

            "If you give up, that's the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA89")

    label("loc_A64B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_A684")

    ChrTalk(    #536
        0xFE,
        (
            "#020FThe sound of a bell?\x02\x03",

            "Nice work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA89")

    label("loc_A684")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A75D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_A6E7")

    ChrTalk(    #537
        0xFE,
        (
            "#022FGo ahead and pursue that new info.\x02\x03",

            "I'll stick in here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A75A")

    label("loc_A6E7")


    ChrTalk(    #538
        0xFE,
        (
            "#020FOh, did something come up?\x02\x03",

            "Persistence is critical in questioning.\x01",
            "Keep following it and don't give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A75A")

    Jump("loc_AA89")

    label("loc_A75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A833")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A7C4")

    ChrTalk(    #539
        0xFE,
        (
            "#022FGo ahead and pursue that new info.\x02\x03",

            "I'll stick in here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A830")

    label("loc_A7C4")


    ChrTalk(    #540
        0xFE,
        (
            "#020FWe've got a new line to follow now.\x02\x03",

            "Hopefully we can get some trustworthy\x01",
            "testimony here, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A830")

    Jump("loc_AA89")

    label("loc_A833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_A8AB")

    ChrTalk(    #541
        0xFE,
        (
            "#020FThe suspect remains unclear as always.\x02\x03",

            "It might be about time to expand\x01",
            "our investigative net.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA89")

    label("loc_A8AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_A946")

    ChrTalk(    #542
        0xFE,
        (
            "#020FWe've gathered a lot about the suspect,\x01",
            "but it's still very unclear.\x02\x03",

            "You need to be very careful about\x01",
            "whose testimony you trust.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA89")

    label("loc_A946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_AA09")
    Jc((scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_A9B8")

    ChrTalk(    #543
        0xFE,
        (
            "#020FHey, why are you wastin' time here?\x02\x03",

            "Hurry up and get back to investigating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA06")

    label("loc_A9B8")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #544
        0xFE,
        (
            "#020FDid you find a clue?\x02\x03",

            "If you did, then try pursuing that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA06")

    Jump("loc_AA89")

    label("loc_AA09")


    ChrTalk(    #545
        0xFE,
        (
            "#020FFirst, we need to start by gathering\x01",
            "information on the suspect.\x02\x03",

            "If some clue comes up, follow\x01",
            "up on it immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA89")

    Return()

    # Function_18_A50C end

    def Function_19_AA8A(): pass

    label("Function_19_AA8A")

    EventBegin(0x0)
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x17, 0x101, 0)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AAE6")
    TurnDirection(0x15, 0x101, 0)

    ChrTalk(    #546
        0x15,
        (
            "#052FGot a mark?\x02\x03",

            "#057FSo, who's your suspect?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB3D")

    label("loc_AAE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AB3D")
    TurnDirection(0x16, 0x101, 0)

    ChrTalk(    #547
        0x16,
        (
            "#023FDo you know who the criminal is?\x02\x03",

            "#022FSo, who's your suspect?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3D")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #548
        "\x18Who is the criminal?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "Kuper")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_ABF9")
    OP_CC(0x1, 0x0, "Norman")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ABF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_AC2F")
    OP_CC(0x1, 0x0, "Herio")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_AC66")
    OP_CC(0x1, 0x0, "Ernest")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_AC9D")
    OP_CC(0x1, 0x0, "Murray")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_ACD4")
    OP_CC(0x1, 0x0, "Belden")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACD4")

    OP_CC(0x1, 0x0, "Never mind")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AE8D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADFD")

    ChrTalk(    #549
        0x15,
        (
            "#055FWhaaat...?!\x02\x03",

            "This old guy's the criminal?!\x02\x03",

            "#551FWell, whatever... First, try and\x01",
            "explain why you discounted the\x01",
            "original suspect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE8A")

    label("loc_ADFD")


    ChrTalk(    #550
        0x15,
        (
            "#055FWhaaat...?!\x02\x03",

            "This old guy's the criminal?!\x02\x03",

            "#551FWell, whatever... First, try and\x01",
            "explain why you discounted the\x01",
            "original suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE8A")

    Jump("loc_AFDD")

    label("loc_AE8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AFDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF4A")

    ChrTalk(    #551
        0x16,
        (
            "#023FWhat...?! You think this person's\x01",
            "the culprit?\x02\x03",

            "#025FYou have proof, I hope.\x02\x03",

            "First, explain why you're discounting\x01",
            "the original suspect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFDD")

    label("loc_AF4A")


    ChrTalk(    #552
        0x16,
        (
            "#023FWhat...?! You think this person's\x01",
            "the culprit?\x02\x03",

            "#025FYou have proof, I hope.\x02\x03",

            "First, explain why you're discounting\x01",
            "the original suspect\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFDD")

    OP_A3(0xC)
    Call(1, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_B0A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B047")

    ChrTalk(    #553
        0x15,
        (
            "#050FNext, you need to explain this\x01",
            "suspect's crime.\x02\x03",

            "Do you have any proof?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A0")

    label("loc_B047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B0A0")

    ChrTalk(    #554
        0x16,
        (
            "#027FNext, you need to explain this\x01",
            "suspect's crime.\x02\x03",

            "Do you have any proof?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A0")

    Call(1, 21)

    label("loc_B0A4")

    Jump("loc_B57A")

    label("loc_B0A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B102")

    ChrTalk(    #555
        0x15,
        (
            "#057FThe first suspect, huh?\x02\x03",

            "Do you have any proof?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B143")

    label("loc_B102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B143")

    ChrTalk(    #556
        0x16,
        (
            "#022FThe first suspect, hmm?\x02\x03",

            "Do you have any proof?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B143")

    Call(1, 22)
    Jump("loc_B57A")

    label("loc_B14A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B1B1")

    ChrTalk(    #557
        0x15,
        (
            "#052FOh, the one who found them?\x02\x03",

            "#050FWhy would you think that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1FC")

    label("loc_B1B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B1FC")

    ChrTalk(    #558
        0x16,
        (
            "#023FThe one who found them, is it?\x02\x03",

            "Why would you think that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1FC")

    OP_A3(0xD)
    Call(1, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_B2E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B274")

    ChrTalk(    #559
        0x15,
        (
            "#050FWhat about the original suspect?\x02\x03",

            "Do you have proof that refutes\x01",
            "Kuper's involvement?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2DB")

    label("loc_B274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B2DB")

    ChrTalk(    #560
        0x16,
        (
            "#022FWhat about the original suspect?\x02\x03",

            "Do you have proof that refutes\x01",
            "Kuper's involvement?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2DB")

    OP_A2(0x10)
    Call(1, 20)

    label("loc_B2E2")

    Jump("loc_B57A")

    label("loc_B2E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B380")

    ChrTalk(    #561
        0x15,
        (
            "#050FThe Raven kid, huh?\x02\x03",

            "You got some proof, right?\x02\x03",

            "First, explain the reason you\x01",
            "discounted the original suspect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B403")

    label("loc_B380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B403")

    ChrTalk(    #562
        0x16,
        (
            "#022FThe Raven boy, is it?\x02\x03",

            "You have real proof, yes?\x02\x03",

            "First, explain the reason you \x01",
            "discounted the original suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B403")

    OP_A3(0xC)
    Call(1, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_B4DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B476")

    ChrTalk(    #563
        0x15,
        (
            "#050FNext, you need to explain this\x01",
            "suspect's crime.\x02\x03",

            "What kind of proof do you have?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D8")

    label("loc_B476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B4D8")

    ChrTalk(    #564
        0x16,
        (
            "#022FNext, you need to explain this\x01",
            "suspect's crime.\x02\x03",

            "What kind of proof do you have?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D8")

    Call(1, 24)

    label("loc_B4DC")

    Jump("loc_B57A")

    label("loc_B4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B52E")

    ChrTalk(    #565
        0x15,
        (
            "#050FWhat, changed your mind?\x02\x03",

            "Well, go investigate more, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B57A")

    label("loc_B52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B57A")

    ChrTalk(    #566
        0x16,
        (
            "#020FWhat, changed your mind?\x02\x03",

            "Well, go investigate more, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B57A")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x17, 255)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    # Function_19_AA8A end

    def Function_20_B590(): pass

    label("Function_20_B590")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #567
        "\x18What refutes Kuper's involvement?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: C'mon, it's obvious!")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_B697")
    OP_CC(0x1, 0x0, "Testimony: He heard the sound from outside.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_B6E3")
    OP_CC(0x1, 0x0, "Fact: He has a solid alibi.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B6E3")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B888")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #568
        (
            "\x07\x05Estelle tried to put together a reasonable explanation\x01",
            "for the crime.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B802")

    ChrTalk(    #569
        0x15,
        (
            "#053FNope, this ain't even worth talkin'\x01",
            "about.\x02\x03",

            "Go investigate again, THOROUGHLY\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B864")

    label("loc_B802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B864")

    ChrTalk(    #570
        0x16,
        (
            "#025FThis isn't even worth talking about...\x02\x03",

            "Go investigate again, in greater detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B864")


    ChrTalk(    #571
        0x101,
        "#1007FEep. Understood...\x02",
    )

    CloseMessageWindow()
    OP_A3(0xC)
    Jump("loc_BF03")

    label("loc_B888")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA99")

    ChrTalk(    #572
        0x101,
        (
            "#1002FWhen the loud sound was heard,\x01",
            "he said he was still outside.\x02\x03",

            "If that was the sound of the crime\x01",
            "being committed, then we can remove\x01",
            "Kuper from the list of suspects.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B9E7")

    ChrTalk(    #573
        0x15,
        (
            "#551FThat's just their interpretation.\x02\x03",

            "#057FWe're just supposed to swallow it?\x01",
            "Go ask around more and come back\x01",
            "when you can prove it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA7A")

    label("loc_B9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BA7A")

    ChrTalk(    #574
        0x16,
        (
            "#025FThat's just their interpretation.\x02\x03",

            "#022FWe're just supposed to accept it?\x01",
            "Go ask around more and come back\x01",
            "when you can prove it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA7A")


    ChrTalk(    #575
        0x101,
        "#1007FUnderstood...\x02",
    )

    CloseMessageWindow()
    OP_A3(0xC)
    Jump("loc_BF03")

    label("loc_BA99")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF03")

    ChrTalk(    #576
        0x101,
        (
            "#1002FKuper was outside when the sound\x01",
            "was heard.\x02\x03",

            "Norman's testimony corroborates this,\x01",
            "so we can say for sure it's accurate.\x02\x03",

            "If that was the sound of the crime being\x01",
            "committed, then there's a very small\x01",
            "chance Kuper is the criminal.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BC03")

    ChrTalk(    #577
        0x15,
        (
            "#053FI see...\x02\x03",

            "And at the same time, we can also\x01",
            "throw out any suspicion of Herio.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC6F")

    label("loc_BC03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BC6F")

    ChrTalk(    #578
        0x16,
        (
            "#022FThat's a logical interpretation.\x02\x03",

            "And the same thing also absolves\x01",
            "Herio of any suspicion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_BEBC")
    OP_A3(0x10)

    ChrTalk(    #579
        0x101,
        (
            "#1002FYep.\x02\x03",

            "Herio had met up with Norman,\x01",
            "so that's sure...\x02\x03",

            "#1015FUm... Wait!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BD2A")

    ChrTalk(    #580
        0x15,
        (
            "#057FWhy are you agreeing?\x02\x03",

            "You just said Herio was the criminal,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD91")

    label("loc_BD2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BD91")

    ChrTalk(    #581
        0x16,
        (
            "#025F*sigh* Why are you agreeing...?\x02\x03",

            "You just said a bit ago that Herio\x01",
            "was the criminal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD91")


    ChrTalk(    #582
        0x101,
        (
            "#1008FAhaha... Oops.\x02\x03",

            "I'm getting confused, sorry. I'm not\x01",
            "sure what I'm saying, either.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BE45")

    ChrTalk(    #583
        0x15,
        (
            "#053FOnce you've put your story in order,\x01",
            "come back.\x02\x03",

            "Then we'll talk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEA6")

    label("loc_BE45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BEA6")

    ChrTalk(    #584
        0x16,
        (
            "#026FGo and put your story in order.\x01",
            "When you're ready, come back.\x02\x03",

            "We'll talk then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEA6")


    ChrTalk(    #585
        0x101,
        "#1007FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF03")

    label("loc_BEBC")


    ChrTalk(    #586
        0x101,
        (
            "#1015FYeah, it does.\x02\x03",

            "Herio met up with Norman, so we're sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_BF03")

    Return()

    # Function_20_B590 end

    def Function_21_BF04(): pass

    label("Function_21_BF04")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #587
        "\x18What explains the suspect's crime?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: C'mon, it's obvious!")
    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #588
        (
            "\x07\x05Estelle tried to put together a reasonable explanation\x01",
            "for the crime.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C082")

    ChrTalk(    #589
        0x15,
        (
            "#053FNope, this ain't even worth talkin'\x01",
            "about.\x02\x03",

            "Go investigate again, THOROUGHLY\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0E4")

    label("loc_C082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C0E4")

    ChrTalk(    #590
        0x16,
        (
            "#025FThis isn't even worth talking about...\x02\x03",

            "Go investigate again, in greater detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0E4")


    ChrTalk(    #591
        0x101,
        "#1007FEep. Understood...\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_21_BF04 end

    def Function_22_C103(): pass

    label("Function_22_C103")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #592
        "\x18What explains Kuper's involvement?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: It just makes sense!")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C204")
    OP_CC(0x1, 0x0, "Testimony: He was angry at the time.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C204")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_C250")
    OP_CC(0x1, 0x0, "Fact: He has a solid alibi.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C250")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C328")

    ChrTalk(    #593
        0x101,
        (
            "#1002FThe situation at the time of the\x01",
            "crime is pretty damning.\x02\x03",

            "Considering the disturbance on the bridge,\x01",
            "I think we have plenty of motive, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C57C")

    label("loc_C328")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C461")

    ChrTalk(    #594
        0x101,
        (
            "#1002FFirst, the situation at the time\x01",
            "of the crime is pretty damning.\x02\x03",

            "Also, I think we can all agree he\x01",
            "has plenty of motive.\x02\x03",

            "The disturbance at the bridge was\x01",
            "recent, and it's only natural that he'd\x01",
            "still be angry.\x02\x03",

            "I also heard from an affiliate that the\x01",
            "suspect seemed angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C57C")

    label("loc_C461")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C57C")

    ChrTalk(    #595
        0x101,
        (
            "#1002FKuper was outside when the sound\x01",
            "was heard.\x02\x03",

            "Norman's testimony corroborates this,\x01",
            "so we can say for sure it's accurate.\x02\x03",

            "If that was the sound of the crime being\x01",
            "committed, then there's a very small\x01",
            "chance Kuper is the criminal.\x02\x03",

            "#1015FUm... Wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C57C")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C77D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C600")

    ChrTalk(    #596
        0x15,
        (
            "#053FYou sure you got your facts straight?\x02\x03",

            "In that case, of course Kuper isn't the\x01",
            "criminal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C665")

    label("loc_C600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C665")

    ChrTalk(    #597
        0x16,
        (
            "#025FWhat are you even trying to say?\x02\x03",

            "In that case, of course Kuper isn't the\x01",
            "criminal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C665")


    ChrTalk(    #598
        0x101,
        (
            "#1008FAhaha... Oops.\x02\x03",

            "I'm getting confused, sorry. I'm not\x01",
            "sure what I'm saying, either.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C719")

    ChrTalk(    #599
        0x15,
        (
            "#053FOnce you've put your story in order,\x01",
            "come back.\x02\x03",

            "Then we'll talk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C77A")

    label("loc_C719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C77A")

    ChrTalk(    #600
        0x16,
        (
            "#026FGo and put your story in order.\x01",
            "When you're ready, come back.\x02\x03",

            "We'll talk then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C77A")

    Jump("loc_C9F1")

    label("loc_C77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C854")

    ChrTalk(    #601
        0x15,
        (
            "#053FYeah, that's true, but...\x02\x03",

            "#050FThe points you've raised don't refute\x01",
            "other possibilities.\x02\x03",

            "In other words, someone might have\x01",
            "come to the room before him.\x02\x03",

            "Can you say that possibility is zero?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C927")

    label("loc_C854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C927")

    ChrTalk(    #602
        0x16,
        (
            "#026FYes, that's true, but...\x02\x03",

            "#022FThe points you've raised don't refute\x01",
            "other possibilities.\x02\x03",

            "In other words, someone might have\x01",
            "come to the room before him.\x02\x03",

            "Can you say that possibility is zero?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C927")


    ChrTalk(    #603
        0x101,
        "#1015FW-Well...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C992")

    ChrTalk(    #604
        0x15,
        (
            "#053FGo investigate more.\x02\x03",

            "We'll talk once you gone over things again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9F1")

    label("loc_C992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C9F1")

    ChrTalk(    #605
        0x16,
        (
            "#027FWell, then, go investigate more.\x02\x03",

            "We'll talk once you gone over things again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9F1")


    ChrTalk(    #606
        0x101,
        "#1007FUnderstood.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_22_C103 end

    def Function_23_CA09(): pass

    label("Function_23_CA09")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #607
        "\x18What explains Herio's involvement?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: C'mon, it's obvious!")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_CB18")
    OP_CC(0x1, 0x0, "Testimony: He visited the crime scene after lunch.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CB18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_CB76")
    OP_CC(0x1, 0x0, "Fact: He visited the crime scene after lunch.")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CB76")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #608
        (
            "\x07\x05Estelle tried to put together a reasonable explanation\x01",
            "for the crime.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CC95")

    ChrTalk(    #609
        0x15,
        (
            "#053FNope, this ain't even worth talkin'\x01",
            "about.\x02\x03",

            "Go investigate again, THOROUGHLY\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF7")

    label("loc_CC95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CCF7")

    ChrTalk(    #610
        0x16,
        (
            "#025FThis isn't even worth talking about...\x02\x03",

            "Go investigate again, in greater detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF7")


    ChrTalk(    #611
        0x101,
        "#1007FEep. Understood...\x02",
    )

    CloseMessageWindow()
    OP_A3(0xD)
    Jump("loc_CEFC")

    label("loc_CD1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDDB")

    ChrTalk(    #612
        0x101,
        (
            "#1002FThere's a witness who saw Herio go to the\x01",
            "second floor before the assault happened.\x02\x03",

            "Furthermore, he himself neglected to\x01",
            "mention it in his own testimony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEFC")

    label("loc_CDDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEFC")

    ChrTalk(    #613
        0x101,
        (
            "#1010FThere's a witness who saw Herio go to\x01",
            "the second floor before the case.\x02\x03",

            "Furthermore, he himself neglected to\x01",
            "mention it in his own testimony.\x02\x03",

            "#1002FThe fact that he's hiding that he went to\x01",
            "the scene of the crime is almost the\x01",
            "same as saying he did it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF16")
    Jump("loc_D079")

    label("loc_CF16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CF72")

    ChrTalk(    #614
        0x15,
        (
            "#050FSo there's evidence that puts\x01",
            "suspicion on him.\x02\x03",

            "...How about a motive?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFCC")

    label("loc_CF72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CFCC")

    ChrTalk(    #615
        0x16,
        (
            "#020FSo there's evidence that casts\x01",
            "suspicion on him.\x02\x03",

            "...How about a motive?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFCC")


    ChrTalk(    #616
        0x101,
        (
            "#1015FApparently, he and the victim are rivals\x01",
            "over who's the #2 in the election camp.\x02\x03",

            "I think it's weak as a motive, but given\x01",
            "the situation I can't say for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_D079")

    Return()

    # Function_23_CA09 end

    def Function_24_D07A(): pass

    label("Function_24_D07A")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #617
        "\x18What explains Belden's involvement?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: He just...is?")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_D10F")
    OP_CC(0x1, 0x0, "Fact: He has no alibi.")

    label("loc_D10F")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2A8")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #618
        (
            "\x07\x05Estelle tried to put together a reasonable explanation\x01",
            "for the crime.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D224")

    ChrTalk(    #619
        0x15,
        (
            "#053FNope, this ain't even worth talkin'\x01",
            "about.\x02\x03",

            "Go investigate again, THOROUGHLY\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D286")

    label("loc_D224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D286")

    ChrTalk(    #620
        0x16,
        (
            "#025FThis isn't even worth talking about...\x02\x03",

            "Go investigate again, in greater detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D286")


    ChrTalk(    #621
        0x101,
        "#1007FEep. Understood...\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_D2A8")


    ChrTalk(    #622
        0x101,
        (
            "#1002FThe proof is his alibi.\x02\x03",

            "I have valuable testimony that\x01",
            "refutes his alibi.\x02\x03",

            "#1015FKuper and Herio have already\x01",
            "been cleared as the culprits, so...\x02\x03",

            "This person remains as the final\x01",
            "possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D430")

    ChrTalk(    #623
        0x15,
        (
            "#053FYeah, by process of elimination it\x01",
            "does turn out that way.\x02\x03",

            "#050FUltimately, though, that's nothin'\x01",
            "but circumstantial evidence.\x02\x03",

            "Do you have any more decisive proof?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4E3")

    label("loc_D430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D4E3")

    ChrTalk(    #624
        0x16,
        (
            "#026FYes, it does look that way by\x01",
            "process of elimination.\x02\x03",

            "#022FUltimately, though, that's nothing\x01",
            "but circumstantial evidence.\x02\x03",

            "Do you have any more decisive proof?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4E3")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #625
        (
            "\x18What evidence supports the theory\x01",
            "that Belden is the criminal?\x02",
        )
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "Instinct: Lucky guess?")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_D5AC")
    OP_CC(0x1, 0x0, "Contradiction: He knew about the special paella.")

    label("loc_D5AC")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D774")

    ChrTalk(    #626
        0x101,
        (
            "#1007FUh... You ask, but..\x02\x03",

            "I don't have anything particular.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D6B9")

    ChrTalk(    #627
        0x15,
        (
            "#053FI see...\x02\x03",

            "#050FThen once more, go over everything\x01",
            "you know.\x02\x03",

            "It's come down to the last bit. We\x01",
            "should be able to solve this soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D74E")

    label("loc_D6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D74E")

    ChrTalk(    #628
        0x16,
        (
            "#026FI see...\x02\x03",

            "#027FThen once more, go over everything\x01",
            "you know.\x02\x03",

            "We've come down to the last bit. We\x01",
            "should be able to solve this soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D74E")


    ChrTalk(    #629
        0x101,
        "#1002FYeah, I'll do my best.\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_D774")


    ChrTalk(    #630
        0x101,
        (
            "#1015FI don't know if it's decisive, but...\x02\x03",

            "Something did bother me, and that's\x01",
            "the testimony about the special paella.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D81B")

    ChrTalk(    #631
        0x15,
        "#052FOh, and what's that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D843")

    label("loc_D81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D843")

    ChrTalk(    #632
        0x16,
        "#023FAnd what's this about?\x02",
    )

    CloseMessageWindow()

    label("loc_D843")


    ChrTalk(    #633
        0x101,
        (
            "#1002FYeah, so Belden testified that he ate\x01",
            "lunch on the first floor, but...\x02\x03",

            "Somehow, he saw the paella Norman ate.\x02\x03",

            "He even knew that Norman barely ate it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D941")

    ChrTalk(    #634
        0x15,
        (
            "#057FIn other words, he went to the second floor.\x02\x03",

            "That what you're sayin'?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D99C")

    label("loc_D941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D99C")

    ChrTalk(    #635
        0x16,
        (
            "#022FIn other words, he went to the second floor.\x02\x03",

            "Is that what you're saying?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D99C")


    ChrTalk(    #636
        0x101,
        "#1002FYeah...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DA5D")

    ChrTalk(    #637
        0x15,
        (
            "#053F...\x02\x03",

            "#057F...All right, I get it.\x02\x03",

            "Let's call Belden in and hear\x01",
            "what he's got to say.\x02\x03",

            "We can't go straight to an arrest\x01",
            "with the proof we have on hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB24")

    label("loc_DA5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DB24")

    ChrTalk(    #638
        0x16,
        (
            "#026F...All right. I'm satisfied.\x02\x03",

            "#022FIn this case, we'll have to call him in\x01",
            "and hear what he has to say first.\x02\x03",

            "We can't go straight to an arrest\x01",
            "with the proof we have on hand.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB24")


    ChrTalk(    #639
        0x101,
        "#1002FO-Okay... Got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(1, 25)
    Return()

    # Function_24_D07A end

    def Function_25_DB51(): pass

    label("Function_25_DB51")

    OP_6D(-44480, 0, 26180, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(72000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF, -46590, 0, 26370, 105)
    SetChrPos(0x101, -44610, 0, 25830, 300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DBCF")
    SetChrPos(0x15, -44620, 0, 24750, 300)
    OP_4A(0x15, 0)
    Jump("loc_DBEB")

    label("loc_DBCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DBEB")
    SetChrPos(0x16, -44620, 0, 24750, 300)
    OP_4A(0x16, 0)

    label("loc_DBEB")

    OP_4A(0xF, 255)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #640
        0xF,
        "#1PWh-What?! Why did you call me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #641
        0xF,
        "#1PI didn't do anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #642
        0x101,
        (
            "#1016F#7PNow, calm down.\x02\x03",

            "Nothing's been decided here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DCDE")

    ChrTalk(    #643
        0x15,
        (
            "#050F#4PIf you help us with the investigation,\x01",
            "you can go home right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD3B")

    label("loc_DCDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DD3B")

    ChrTalk(    #644
        0x16,
        (
            "#020F#4PIf you can help out with the investigation,\x01",
            "you can go home right after.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD3B")


    ChrTalk(    #645
        0xF,
        "#1PH-Help...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #646
        0x101,
        (
            "#1002F#7PYeah, we just want you to be\x01",
            "frank with us.\x02\x03",

            "Where did you go after lunch?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #647
        0xF,
        "#1PL-Like I said, I was in the basement...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DE47")

    ChrTalk(    #648
        0x15,
        (
            "#057F#4PBull.\x02\x03",

            "As long as you keep lyin',\x01",
            "you're not gettin' out of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEAB")

    label("loc_DE47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DEAB")

    ChrTalk(    #649
        0x16,
        (
            "#026F#4PJust to warn you...\x02\x03",

            "As long as you keep lying,\x01",
            "you're not getting out of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEAB")

    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #650
        0xF,
        "#1PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #651
        0x101,
        (
            "#1002F#7PYou weren't in the basement the\x01",
            "whole time.\x02\x03",

            "We already know that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #652
        0xF,
        "#1P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DFBC")

    ChrTalk(    #653
        0x15,
        (
            "#050F#4PIf you didn't do anything wrong, then\x01",
            "just be honest and tell the truth.\x02\x03",

            "#053FOr is the truth too scary to admit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E050")

    label("loc_DFBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E050")

    ChrTalk(    #654
        0x16,
        (
            "#022F#4PIf you didn't do anything wrong, then\x01",
            "you should be able to be honest and\x01",
            "tell the truth.\x02\x03",

            "Or is the truth too scary too admit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E050")


    ChrTalk(    #655
        0xF,
        "#1PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #656
        0xF,
        "#1PF-Fine... I'll talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #657
        0xF,
        "#1PToday...after lunch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #658
        0xF,
        "#1PI... I went to the office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #659
        0xF,
        "#1PI went to go clean up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0x101,
        (
            "#1002F#7PClean up...?\x02\x03",

            "So the person who returned\x01",
            "the plates to the front was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #661
        0xF,
        "#1PYeah, it was me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #662
        0xF,
        (
            "#1PEveryone seemed busy, so I figured\x01",
            "I'd clean up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #663
        0xF,
        (
            "#1PWhile I was cleaning up, I thought\x01",
            "I'd tidy the office, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #664
        0xF,
        "#1P*sigh* I didn't think that'd happen...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #665
        0x101,
        (
            "#1004F#7PHuh...?\x02\x03",

            "H-Hold on, you're not making sense.\x02\x03",

            "#1002FYou just cleaned up after, right?\x02\x03",

            "Why does that have anything to\x01",
            "do with the case?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E2D9")

    ChrTalk(    #666
        0x15,
        "#050F#4P...I've got an idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E302")

    label("loc_E2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E302")

    ChrTalk(    #667
        0x16,
        "#027F#4P...I've got an idea.\x02",
    )

    CloseMessageWindow()

    label("loc_E302")


    ChrTalk(    #668
        0xF,
        "#1PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #669
        0xF,
        "#1PActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 0)
    OP_4A(0x14, 0)
    OP_4A(0xE, 0)
    OP_4A(0x17, 0)
    SetChrPos(0xB, -3200, 0, 81000, 180)
    SetChrPos(0x14, -2140, 0, 81000, 180)
    SetChrPos(0xE, -1300, 0, 80130, 215)
    SetChrPos(0xF, -2710, 0, 79250, 0)
    SetChrPos(0x101, -3400, 0, 77780, 0)
    SetChrPos(0x17, -3150, 0, 76370, 0)
    SetChrPos(0x105, -2150, 0, 76170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E412")
    SetChrPos(0x15, -2400, 0, 77580, 0)
    Jump("loc_E42A")

    label("loc_E412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E42A")
    SetChrPos(0x16, -2400, 0, 77580, 0)

    label("loc_E42A")

    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #670
        0xB,
        "#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #671
        0xB,
        (
            "#6PI understand Belden came to this\x01",
            "room to clean, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #672
        0xB,
        "#6PI'm not sure how that correlates.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #673
        0xB,
        (
            "#6PWhat does that have to do with the\x01",
            "assault on Dels?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #674
        0x101,
        (
            "#1007F#4PIt has a lot to do with it.\x02\x03",

            "#1000FWell, let's hear him say it himself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E582")

    ChrTalk(    #675
        0x15,
        "#050F...Hey, go tell 'em.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #676
        0xF,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5B5")

    label("loc_E582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E5B5")

    ChrTalk(    #677
        0x16,
        "#020F...Go on, explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #678
        0xF,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()

    label("loc_E5B5")


    ChrTalk(    #679
        0xF,
        (
            "Well, once I finished cleaning the\x01",
            "room, I thought I'd head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #680
        0xF,
        (
            "But since I'd tidied up a lot of stuff,\x01",
            "the room was real dusty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #681
        0xF,
        (
            "I thought I'd open the balcony door\x01",
            "to air it out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #682
        0xF,
        "My hands were full of plates...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0xF,
        "I... I didn't have any choice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #684
        0xF,
        (
            "So I, um, kicked the door as hard\x01",
            "as I could.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(30)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_43(0x14, 0x1, 0x1, 0x1A)
    Sleep(30)
    OP_43(0xE, 0x1, 0x1, 0x1A)
    OP_43(0xB, 0x1, 0x1, 0x1A)

    def lambda_E783():
        OP_6D(-1140, 0, 84170, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E783)

    def lambda_E79B():
        OP_6B(3030, 2000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E79B)
    OP_67(0, 5480, -10000, 2000)

    ChrTalk(    #685
        0x1A,
        "Wait, you mean the door...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #686
        0x101,
        (
            "#1007F#5PYep, it's exactly what you think.\x02\x03",

            "That door is the criminal that\x01",
            "knocked out Dels.\x02\x03",

            "#1002FThe door flying open slammed\x01",
            "right into the back of your head.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E8D6")

    ChrTalk(    #687
        0x15,
        (
            "#551F#2PIn other words, the truth of the case\x01",
            "is 'an unlucky accident.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E92A")

    label("loc_E8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E92A")

    ChrTalk(    #688
        0x16,
        (
            "#025F#2PIn other words, the truth of the case\x01",
            "is 'an unlucky accident.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E92A")

    Sleep(400)
    OP_59()
    Fade(1000)
    OP_6D(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #689
        0x14,
        "#6PWhat?! So then...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 800)
    Sleep(400)

    ChrTalk(    #690
        0x14,
        "#6PI'm innocent, right?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 225, 400)
    Sleep(400)

    ChrTalk(    #691
        0xE,
        "Seems like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0x14,
        (
            "#6P*pheeew* Man, oh, man.\x01",
            "Finally free and clear.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(400)

    ChrTalk(    #693
        0xB,
        "#6PStill, what a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0xB,
        (
            "#6PWhy didn't you volunteer this\x01",
            "information at the beginning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #695
        0xB,
        (
            "#6PIf you'd just told us the truth, things\x01",
            "wouldn't have gone nearly this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #696
        0xF,
        "I-I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #697
        0x101,
        (
            "#1016F#4PC'mon, he's telling the truth now.\x01",
            "Give him a break, okay?\x02\x03",

            "He had the courage to talk about it\x01",
            "in the end, so everything worked out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #698
        0x1A,
        (
            "As the victim here, I'd just like to\x01",
            "forgive and forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #699
        0x1A,
        (
            "It's already clear that this was all\x01",
            "a misunderstanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #700
        0x1A,
        (
            "Of course, I'd like him to be a bit\x01",
            "more careful opening doors in the\x01",
            "future, if he could...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x1A, 400)

    ChrTalk(    #701
        0xF,
        "#4PDels, I'm really sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x14, 400)

    ChrTalk(    #702
        0xF,
        (
            "And you too, Kuper. You almost got\x01",
            "turned into a criminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0xF, 400)

    ChrTalk(    #703
        0x14,
        "#6PYou don't need to worry about me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #704
        0x14,
        (
            "#6PI'm in the clear, and that's good\x01",
            "enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #705
        0x17,
        "#031F#2PWell! That settles things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #706
        0x105,
        "#040F#2PThank goodness.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EE82")

    ChrTalk(    #707
        0x15,
        (
            "#050FAlso, Belden...\x02\x03",

            "Whatever you decide to do in life,\x01",
            "know that the decision is yours and\x01",
            "yours alone. I know you can do it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x15, 400)

    ChrTalk(    #708
        0xF,
        "R-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #709
        0x15,
        (
            "#051FYeah, make sure you keep it up.\x02\x03",

            "#053F...Well, that's our report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEAE")

    label("loc_EE82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_EEAE")

    ChrTalk(    #710
        0x16,
        "#020F...And that is our report.\x02",
    )

    CloseMessageWindow()

    label("loc_EEAE")


    ChrTalk(    #711
        0xB,
        "#6PBracers... I'm sorry for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #712
        0xB,
        (
            "#6PIt seems we've taken up a great deal\x01",
            "of your time over just a big mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #713
        0x101,
        (
            "#1000F#4PNo, don't worry about it.\x02\x03",

            "This is part of the job too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EFA1")

    ChrTalk(    #714
        0x15,
        "#050FWell, then, we're off.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 400)
    Jump("loc_EFD0")

    label("loc_EFA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_EFD0")

    ChrTalk(    #715
        0x16,
        "#020FWell, then, pardon us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x16, 400)

    label("loc_EFD0")

    OP_8C(0xF, 180, 400)

    ChrTalk(    #716
        0xF,
        "Thank you, guys...so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #717
        0xB,
        "#6PReally, I'm very sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #718
        0x14,
        "#6PTake care!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_DB51 end

    def Function_26_F042(): pass

    label("Function_26_F042")

    OP_8B(0xFE, 0xFFFFFB8C, 0x148CA, 0x190)
    Return()

    # Function_26_F042 end

    def Function_27_F050(): pass

    label("Function_27_F050")

    SetChrPos(0xFE, 5750, 2250, 380, 262)
    OP_8E(0xFE, 0x2C6, 0x0, 0x15E, 0x5DC, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_27_F050 end

    def Function_28_F07D(): pass

    label("Function_28_F07D")

    SetChrPos(0xFE, 6330, 2250, -170, 281)
    OP_8E(0xFE, 0x582, 0x0, 0xFFFFFF42, 0x5DC, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_F07D end

    def Function_29_F0AA(): pass

    label("Function_29_F0AA")

    OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF510, 0x0, 0xC6C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF308, 0x0, 0x2526, 0x7D0, 0x0)
    Return()

    # Function_29_F0AA end

    def Function_30_F0E7(): pass

    label("Function_30_F0E7")

    OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFF42, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6AA, 0x0, 0xA64, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF5C4, 0x0, 0x201C, 0x7D0, 0x0)
    Return()

    # Function_30_F0E7 end

    def Function_31_F124(): pass

    label("Function_31_F124")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_31_F124 end

    def Function_32_F139(): pass

    label("Function_32_F139")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_32_F139 end

    def Function_33_F14E(): pass

    label("Function_33_F14E")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_33_F14E end

    def Function_34_F163(): pass

    label("Function_34_F163")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_34_F163 end

    def Function_35_F178(): pass

    label("Function_35_F178")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 500, 0, 76980, 255)

    def lambda_F19A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F19A)
    OP_8E(0xFE, 0xFFFFFF1A, 0x0, 0x12CC8, 0x7D0, 0x0)
    Return()

    # Function_35_F178 end

    def Function_36_F1BB(): pass

    label("Function_36_F1BB")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x13902, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_36_F1BB end

    def Function_37_F1EF(): pass

    label("Function_37_F1EF")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x133BC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_37_F1EF end

    def Function_38_F223(): pass

    label("Function_38_F223")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0x132F4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_38_F223 end

    def Function_39_F257(): pass

    label("Function_39_F257")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0x12E3A, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_39_F257 end

    def Function_40_F28B(): pass

    label("Function_40_F28B")

    Call(1, 35)
    OP_8C(0xFE, 90, 400)
    OP_72(0x6, 0x800)
    OP_70(0x6, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x800)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF79A, 0x0, 0x12D72, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_40_F28B end

    def Function_41_F2E4(): pass

    label("Function_41_F2E4")

    TurnDirection(0xFE, 0x18, 400)
    Return()

    # Function_41_F2E4 end

    def Function_42_F2EC(): pass

    label("Function_42_F2EC")

    TurnDirection(0xFE, 0x18, 400)
    Return()

    # Function_42_F2EC end

    def Function_43_F2F4(): pass

    label("Function_43_F2F4")

    OP_8C(0x104, 180, 400)
    SetChrChipByIndex(0x104, 10)
    SetChrFlags(0x104, 0x2)
    OP_99(0x104, 0x0, 0x3, 0x4B0)
    Sleep(200)
    OP_99(0x104, 0x3, 0xA, 0x4B0)
    Return()

    # Function_43_F2F4 end

    def Function_44_F31D(): pass

    label("Function_44_F31D")

    OP_6D(130, 0, 4860, 1000)
    OP_6D(-170, 0, 2320, 2000)
    Return()

    # Function_44_F31D end

    SaveToFile()

Try(main)
