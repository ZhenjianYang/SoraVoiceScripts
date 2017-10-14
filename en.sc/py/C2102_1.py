from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C2102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_635",          # 01, 1
        "Function_2_BE0",          # 02, 2
        "Function_3_BF2",          # 03, 3
        "Function_4_C1D",          # 04, 4
        "Function_5_C48",          # 05, 5
        "Function_6_C73",          # 06, 6
        "Function_7_C9E",          # 07, 7
        "Function_8_CF0",          # 08, 8
        "Function_9_D46",          # 09, 9
        "Function_10_DFB",         # 0A, 10
        "Function_11_158D",        # 0B, 11
        "Function_12_227D",        # 0C, 12
        "Function_13_230B",        # 0D, 13
        "Function_14_2A11",        # 0E, 14
        "Function_15_2A7C",        # 0F, 15
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Call(1, 7)
    FadeToBright(2000, 0)
    Call(1, 8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #0
        0x101,
        "#1004F#4PWhoa!\x02",
    )

    CloseMessageWindow()
    Call(1, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_181")

    ChrTalk(    #1
        0x101,
        "#1020F#2PIt really IS active...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_154")

    ChrTalk(    #2
        0x106,
        "#057FJust like we heard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17E")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_17E")

    ChrTalk(    #3
        0x103,
        "#022FI see. Just as we heard.\x02",
    )

    CloseMessageWindow()

    label("loc_17E")

    Jump("loc_260")

    label("loc_181")


    ChrTalk(    #4
        0x101,
        "#1020F#2PSomething's...moving!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_206")

    ChrTalk(    #5
        0x106,
        (
            "#052FWell, it, uh, is an ancient relic.\x02\x03",

            "It shouldn't really work anymore, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_260")

    ChrTalk(    #6
        0x103,
        (
            "#022FIt is an ancient relic, remember.\x02\x03",

            "It's supposed to be long dead, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_450")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_31D")

    ChrTalk(    #7
        0x104,
        (
            "#031FAh, but it is possessed of such a\x01",
            "mythic light.\x02\x03",

            "Heh... I can feel the wisdom of\x01",
            "the ancients washing over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x127,
        "#151FYeah! It's sooooooo pretty. ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B1")

    label("loc_31D")


    ChrTalk(    #9
        0x104,
        (
            "#031FSo this is an ancient device, then.\x02\x03",

            "Heh, that explains the mythic light\x01",
            "I feel washing over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x127,
        "#151FYeah! It's sooooooo pretty. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_3B1")

    TurnDirection(0x101, 0x127, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#1007F#2PHow are you two not the least\x01",
            "bit freaked out about this?\x02\x03",

            "#2PI guess it doesn't look dangerous,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4CB")

    ChrTalk(    #12
        0x101,
        (
            "#1015F#2PBut if something like this starts\x01",
            "up again...\x02\x03",

            "#2PI guess it doesn't look dangerous,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_4CB")


    ChrTalk(    #13
        0x101,
        (
            "#1020F#2PBut why's it shining, then?\x02\x03",

            "#1015FI guess it doesn't look dangerous,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_59C")

    ChrTalk(    #14
        0x106,
        (
            "#050FMaybe not, but don't let your guard down.\x02\x03",

            "Anything could happen at this point,\x01",
            "so stay alert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_610")

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_610")

    ChrTalk(    #15
        0x103,
        (
            "#022FMaybe...but don't let your guard down,\x01",
            "even if it 'looks' safe.\x02\x03",

            "We need to be ready for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_610")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #16
        0x101,
        "#1002F#2PRight.\x02",
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_635(): pass

    label("Function_1_635")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Call(1, 7)
    FadeToBright(2000, 0)
    Call(1, 8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #17
        0x101,
        "#1004F#4PWhoa!\x02",
    )

    CloseMessageWindow()

    label("loc_68F")

    Call(1, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7")

    ChrTalk(    #18
        0x101,
        "#1020F#2PIt really IS active...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EF")

    label("loc_6C7")


    ChrTalk(    #19
        0x101,
        "#1002F#2PSo it really IS active...\x02",
    )

    CloseMessageWindow()

    label("loc_6EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_724")

    ChrTalk(    #20
        0x106,
        "#057FJust like we heard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_74E")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #21
        0x103,
        "#022FI see. Just as we heard.\x02",
    )

    CloseMessageWindow()

    label("loc_74E")


    ChrTalk(    #22
        0x104,
        (
            "#031FAh, but it is possessed of such a\x01",
            "mythic light.\x02\x03",

            "Heh... I can feel the wisdom of\x01",
            "the ancients washing over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x127,
        "#151FYeah! It's sooooooo pretty. ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x101,
        (
            "#1007F#2PHow are you two not the least\x01",
            "bit freaked out about this?\x02\x03",

            "#2POh, whatever. Let's get the picture taken\x01",
            "and get out of here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #25
        0x106,
        (
            "#552FLet's. I'd like to hang around here\x01",
            "as little as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_941")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_941")

    ChrTalk(    #26
        0x103,
        (
            "#025FA good idea. It would be best to not\x01",
            "remain longer than necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_941")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #27
        0x101,
        "#1015F#2PLet's see, where should I take it from...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0A")

    label("loc_983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #28
        0x106,
        (
            "#050FJust like we heard.\x02\x03",

            "Doesn't seem all that dangerous, but let's\x01",
            "take the picture and get this over with.\x02\x03",

            "I'd prefer to not stick around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC7")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(    #29
        0x103,
        (
            "#022FI see. Just as we heard.\x02\x03",

            "It seems safe, for now, but let's get\x01",
            "the picture taken quickly anyway.\x02\x03",

            "It would be wise to leave as soon as we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC7")


    ChrTalk(    #30
        0x101,
        (
            "#1002F#2PRight...\x02\x03",

            "#1015FOkay, so, where should I shoot from?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A")

    OP_59()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #31
        "\x07\x05To take a picture, use the #15IOrbal Camera.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #32
        (
            "\x07\x05Move to where you wish to take a picture from, then select\x01",
            "the #15IOrbal Camera from the [Items] tab in the camp menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_28(0x66, 0x1, 0x1000)
    OP_28(0x66, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_1_635 end

    def Function_2_BE0(): pass

    label("Function_2_BE0")

    OP_6D(70, 0, 8320, 2000)
    Return()

    # Function_2_BE0 end

    def Function_3_BF2(): pass

    label("Function_3_BF2")

    SetChrPos(0xFE, 600, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0x258, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_3_BF2 end

    def Function_4_C1D(): pass

    label("Function_4_C1D")

    SetChrPos(0xFE, -100, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0xFFFFFF9C, 0x0, 0x1450, 0x7D0, 0x0)
    Return()

    # Function_4_C1D end

    def Function_5_C48(): pass

    label("Function_5_C48")

    SetChrPos(0xFE, 400, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0x190, 0x0, 0x1068, 0x7D0, 0x0)
    Return()

    # Function_5_C48 end

    def Function_6_C73(): pass

    label("Function_6_C73")

    SetChrPos(0xFE, -300, -1000, -5960, 0)
    Sleep(400)
    OP_90(0xFE, 0xFFFFFED4, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_6_C73 end

    def Function_7_C9E(): pass

    label("Function_7_C9E")

    SetChrPos(0x101, 600, -10000, -5960, 0)
    SetChrPos(0xF7, -600, -10000, -5960, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEF")
    SetChrPos(0x104, 600, -10000, -6960, 0)
    SetChrPos(0x127, -600, -10000, -6960, 0)

    label("loc_CEF")

    Return()

    # Function_7_C9E end

    def Function_8_CF0(): pass

    label("Function_8_CF0")

    OP_43(0x101, 0x1, 0x1, 0x3)
    Sleep(750)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D0D")
    OP_43(0x106, 0x1, 0x1, 0x4)
    Jump("loc_D1B")

    label("loc_D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D1B")
    OP_43(0x103, 0x1, 0x1, 0x4)

    label("loc_D1B")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D40")
    OP_43(0x104, 0x1, 0x1, 0x5)
    Sleep(750)
    OP_43(0x127, 0x1, 0x1, 0x6)

    label("loc_D40")

    WaitChrThread(0x101, 0x1)
    Return()

    # Function_8_CF0 end

    def Function_9_D46(): pass

    label("Function_9_D46")

    OP_6D(-160, 950, 12910, 4000)
    Sleep(2000)
    OP_43(0x101, 0x2, 0x1, 0x2)

    def lambda_D69():
        OP_90(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D69)
    Sleep(100)

    def lambda_D89():
        OP_90(0xF7, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_D89)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEB")
    Sleep(100)

    def lambda_DB6():
        OP_90(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DB6)
    Sleep(100)

    def lambda_DD6():
        OP_90(0x127, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_DD6)

    label("loc_DEB")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Return()

    # Function_9_D46 end

    def Function_10_DFB(): pass

    label("Function_10_DFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E32")
    SetMapFlags(0x80)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        "Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x80)
    Return()

    label("loc_E32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7F")
    SetMapFlags(0x80)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        "Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x80)
    Return()

    label("loc_E7F")

    SetMapFlags(0x80)
    OP_C2()
    Sleep(30)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)
    OP_8B(0x0, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x1, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x2, 0xFFFFFF2E, 0x3D40, 0x0)
    OP_8B(0x3, 0xFFFFFF2E, 0x3D40, 0x0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEC")
    OP_51(0x9, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_EEC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F05")
    OP_51(0xA, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_F05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1E")
    OP_51(0xB, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_F1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FBB")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F88")

    ChrTalk(    #35
        0x101,
        "#1015FThe pillar is in the way here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB8")

    label("loc_F88")


    ChrTalk(    #36
        0x101,
        "#1015FThe pillar might be in the way here.\x02",
    )

    CloseMessageWindow()

    label("loc_FB8")

    EventEnd(0x3)
    Return()

    label("loc_FBB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109C")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")

    ChrTalk(    #37
        0x101,
        (
            "#1003FThe angle's a bit off.\x02\x03",

            "I need to take the picture more\x01",
            "straight on, I think...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1099")

    label("loc_1040")


    ChrTalk(    #38
        0x101,
        (
            "#1007FThe angle's a bit off.\x02\x03",

            "I ought to take the picture\x01",
            "more from the front. Ish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    EventEnd(0x3)
    Return()

    label("loc_109C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x361A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x42C1D80), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_119C")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #39
        0x101,
        (
            "#1007FEr, this is a bit too close.\x02\x03",

            "I need to back off a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1199")

    label("loc_1150")


    ChrTalk(    #40
        0x101,
        (
            "#1007FEr, this is a bit too close.\x02\x03",

            "Maybe I should back away a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1199")

    EventEnd(0x3)
    Return()

    label("loc_119C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0xBEBC200), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_123A")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F4")

    ChrTalk(    #41
        0x101,
        (
            "#1015FHmm...\x02\x03",

            "I wonder if this is a bit too far?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1237")

    label("loc_11F4")


    ChrTalk(    #42
        0x101,
        (
            "#1015FLesse, from here...\x02\x03",

            "I wonder if this is a bit too far?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1237")

    EventEnd(0x3)
    Return()

    label("loc_123A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_124F")
    OP_A2(0x0)
    Jump("loc_13B2")

    label("loc_124F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1263")
    OP_A2(0x1)
    Jump("loc_13B2")

    label("loc_1263")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12FE")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(    #43
        0x101,
        (
            "#1015FHmm...\x02\x03",

            "I wonder if this is a bit too far?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FB")

    label("loc_12B8")


    ChrTalk(    #44
        0x101,
        (
            "#1015FLesse, from here...\x02\x03",

            "I wonder if this is a bit too far?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FB")

    EventEnd(0x3)
    Return()

    label("loc_12FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1838), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B2")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1366")

    ChrTalk(    #45
        0x101,
        (
            "#1007FEr, this is a bit too close.\x02\x03",

            "Maybe I should back away a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AF")

    label("loc_1366")


    ChrTalk(    #46
        0x101,
        (
            "#1007FEr, this is a bit too close.\x02\x03",

            "Maybe I should back away a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AF")

    EventEnd(0x3)
    Return()

    label("loc_13B2")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F2")

    ChrTalk(    #47
        0x101,
        (
            "#1015FHmmmmm...\x01",
            "This seems okay, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_13F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")

    ChrTalk(    #48
        0x106,
        (
            "#050FHey, Estelle.\x01",
            "How about here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149A")

    label("loc_1429")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(    #49
        0x103,
        "#020FEstelle, how about taking it here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149A")

    label("loc_1465")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #50
        0x104,
        "#030FEstelle. Why not take it here?\x02",
    )

    CloseMessageWindow()

    label("loc_149A")

    OP_8B(0x101, 0x0, 0x3192, 0x1F4)

    ChrTalk(    #51
        0x101,
        "#1011FOh, yeah. This looks like a good spot.\x02",
    )

    CloseMessageWindow()

    label("loc_14D9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Take Picture Here\x01",           # 0
            "Look For Another Place\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154A")
    Call(1, 11)
    Jump("loc_1585")

    label("loc_154A")


    ChrTalk(    #52
        0x101,
        "#1015FI think I'm gonna look around a bit more.\x02",
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_1585")

    EventEnd(0x3)
    ClearMapFlags(0x80)
    Return()

    # Function_10_DFB end

    def Function_11_158D(): pass

    label("Function_11_158D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_51(0x101, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1623")
    OP_8C(0x101, 45, 0)
    SetChrPos(0xF7, -11490, 250, 4670, 0)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1620")
    SetChrPos(0x104, -13060, 250, 3460, 0)
    SetChrPos(0x127, -11130, 250, 2970, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_1620")

    Jump("loc_16E5")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1689")
    OP_8C(0x101, 315, 0)
    SetChrPos(0xF7, 12340, 250, 4740, 338)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1686")
    SetChrPos(0x104, 13400, 250, 3860, 338)
    SetChrPos(0x127, 11220, 250, 3250, 338)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_1686")

    Jump("loc_16E5")

    label("loc_1689")

    OP_8C(0x101, 0, 0)
    SetChrPos(0xF7, 1050, 0, 500, 0)
    TurnDirection(0xF7, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_16E5")
    SetChrPos(0x104, 270, 0, -1000, 0)
    SetChrPos(0x127, -850, 0, 0, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)

    label("loc_16E5")

    OP_69(0x101, 0x0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        (
            "#1006FAll right. I've made up my mind.\x02\x03",

            "#1018FI'll take it.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17A5")

    ChrTalk(    #54
        0x127,
        "#151FGood luck, Esteeeeelle. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_17A5")

    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x101, 1)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x101)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_225D")
    Fade(250)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x127, 400)
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x8, 0x3E8)

    ChrTalk(    #55
        0x127,
        "#153FHuuuuh? Are you giving up?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_188A")

    ChrTalk(    #56
        0x106,
        "#052FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_188A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_18AC")

    ChrTalk(    #57
        0x103,
        "#023FSomething wrong?\x02",
    )

    CloseMessageWindow()

    label("loc_18AC")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1015FNot really... I just realized I don't\x01",
            "need to take the picture.\x02\x03",

            "It may just be coincidence, but we DO\x01",
            "have a pro...of sorts, anyway...with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1987")

    ChrTalk(    #59
        0x106,
        "#051FAhhhh, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_19A9")

    ChrTalk(    #60
        0x103,
        "#021FAh, that's true!\x02",
    )

    CloseMessageWindow()

    label("loc_19A9")


    ChrTalk(    #61
        0x101,
        (
            "#1011FDo you mind?\x02\x03",

            "If I ask Dorothy, I mean.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A36")

    ChrTalk(    #62
        0x106,
        (
            "#051FNah, go ahead.\x02\x03",

            "If you don't think you can do it,\x01",
            "no shame in askin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A87")

    label("loc_1A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1A87")

    ChrTalk(    #63
        0x103,
        (
            "#027FNot at all.\x02\x03",

            "If you're not feeling confident,\x01",
            "go ahead and ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A87")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ask Dorothy\x01",         # 0
            "Do it Yourself\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205F")
    TurnDirection(0x101, 0x127, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1000FSo, Dorothy?\x02\x03",

            "Would you mind taking the picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x127,
        (
            "#151FYeah, yeah, I'll do it!\x02\x03",

            "I'll give it my all! And stuff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1017FHaha! Thanks.\x02\x03",

            "Here's the camera.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CA2")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x127, 0, 0, 4000, 0)
    SetChrPos(0x101, -50, 0, 1280, 0)
    SetChrPos(0xF7, 1050, 0, 500, 0)
    TurnDirection(0xF7, 0x127, 0)
    SetChrPos(0x104, 270, 0, -1000, 0)
    TurnDirection(0x104, 0x127, 0)
    OP_69(0x127, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #67
        0x127,
        "#151FOkaaaaay! Here we goooo. ♪\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x127, 16)
    OP_0D()
    Call(1, 14)

    ChrTalk(    #68
        0x127,
        (
            "#153FAhhh! It's got a scary face!\x02\x03",

            "#151FWell, say cheeeeeeese. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jump("loc_1E81")

    label("loc_1CA2")


    def lambda_1CA8():
        OP_69(0x127, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1CA8)

    def lambda_1CB6():

        label("loc_1CB6")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1CB6")

    QueueWorkItem2(0xF7, 1, lambda_1CB6)

    def lambda_1CC7():

        label("loc_1CC7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1CC7")

    QueueWorkItem2(0x104, 1, lambda_1CC7)

    def lambda_1CD8():

        label("loc_1CD8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1CD8")

    QueueWorkItem2(0x127, 1, lambda_1CD8)
    OP_8E(0x101, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    TurnDirection(0x101, 0x127, 400)
    WaitChrThread(0xF7, 0x2)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #69
        "You gave the #562i to Dorothy.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(    #70
        0x127,
        "#150FOkaaaaay! Here we goooo!\x02",
    )

    CloseMessageWindow()

    def lambda_1D8D():

        label("loc_1D8D")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1D8D")

    QueueWorkItem2(0x101, 1, lambda_1D8D)
    OP_94(0x0, 0x101, 0x10E, 0x320, 0x7D0, 0x0)

    def lambda_1DAD():
        OP_6D(0, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1DAD)

    def lambda_1DC5():

        label("loc_1DC5")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1DC5")

    QueueWorkItem2(0xF7, 1, lambda_1DC5)

    def lambda_1DD6():

        label("loc_1DD6")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1DD6")

    QueueWorkItem2(0x104, 1, lambda_1DD6)
    OP_8E(0x127, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    OP_8E(0x127, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_8C(0x127, 0, 400)
    OP_44(0xF7, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0xF7, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x127, 16)
    OP_0D()
    Call(1, 14)

    ChrTalk(    #71
        0x127,
        (
            "#153FAhhh! It's got a scary face!\x02\x03",

            "#151FWell, say cheeeeeeese. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    label("loc_1E81")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x127, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    SetChrChipByIndex(0x127, 65535)
    OP_8C(0x127, 180, 400)
    Sleep(1000)

    ChrTalk(    #72
        0x127,
        (
            "#151FThanks for waiting!\x02\x03",

            "I got some really angry, sullen,\x01",
            "manly pictures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1016FUm, I see! Good job, Dorothy.\x02",
    )

    CloseMessageWindow()

    def lambda_1F64():
        OP_6D(-850, 0, 1280, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1F64)

    def lambda_1F7C():

        label("loc_1F7C")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1F7C")

    QueueWorkItem2(0x101, 1, lambda_1F7C)

    def lambda_1F8D():

        label("loc_1F8D")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1F8D")

    QueueWorkItem2(0xF7, 1, lambda_1F8D)

    def lambda_1F9E():

        label("loc_1F9E")

        TurnDirection(0xFE, 0x127, 0)
        OP_48()
        Jump("loc_1F9E")

    QueueWorkItem2(0x104, 1, lambda_1F9E)
    OP_8E(0x127, 0xFFFFFCAE, 0x0, 0x500, 0x7D0, 0x0)
    TurnDirection(0x127, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0xF7, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #74
        "\x07\x00Estelle took the #562i back.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #75
        0x101,
        (
            "#1001FThanks!\x02\x03",

            "Looks like we're done, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x8)
    Jump("loc_225A")

    label("loc_205F")


    ChrTalk(    #76
        0x101,
        (
            "#1015F...No, you know what?\x01",
            "I'll do it.\x02\x03",

            "I mean, I'm the one who took this job,\x01",
            "so I should be the one to pull the...\x01",
            "uh, shutter, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x127,
        (
            "#150FYeah! I think this is a great idea,\x01",
            "Estelle!\x02\x03",

            "I know if I had to ask someone else to\x01",
            "take pictures of something this neato,\x01",
            "I'd jump off a cliff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1007FRiiight. Thanks, Dorothy.\x02",
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xFFFFFF2E, 0x3D40, 0x190)

    ChrTalk(    #79
        0x101,
        (
            "#1002FOkay, let's start over.\x02\x03",

            "I'll get my concentration back and\x01",
            "take this picture!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Sleep(400)
    Fade(250)
    SetChrSubChip(0x101, 1)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(1000)
    Call(1, 12)
    OP_28(0x66, 0x1, 0x4)

    label("loc_225A")

    Jump("loc_2267")

    label("loc_225D")

    Call(1, 12)
    OP_28(0x66, 0x1, 0x4)

    label("loc_2267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2276")
    Call(1, 15)

    label("loc_2276")

    Call(1, 13)
    EventEnd(0x0)
    Return()

    # Function_11_158D end

    def Function_12_227D(): pass

    label("Function_12_227D")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x101, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(250)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(400)

    ChrTalk(    #80
        0x101,
        "#1018FAnd all done!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_12_227D end

    def Function_13_230B(): pass

    label("Function_13_230B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_237B")

    ChrTalk(    #81
        0x106,
        (
            "#050FAll right, let's get back to town, then.\x02\x03",

            "Ain't no point in stickin' around\x01",
            "this old wreck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D1")

    label("loc_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(    #82
        0x103,
        (
            "#020FLet's return to town, then.\x02\x03",

            "There's little point in remaining here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D1")

    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(400)

    ChrTalk(    #83
        0x101,
        "#1004F#6PWe're going back already?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_245F")

    ChrTalk(    #84
        0x106,
        (
            "#052FYeah, that was the plan.\x02\x03",

            "There a problem, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A3")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_24A3")

    ChrTalk(    #85
        0x103,
        (
            "#023FWell, yes, that was the plan.\x02\x03",

            "Is there a problem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A3")


    ChrTalk(    #86
        0x101,
        (
            "#1015F#6PNot really a problem, I guess, it's just...\x02\x03",

            "We came all this way, so heading straight\x01",
            "back would be a waste, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(    #87
        0x106,
        (
            "#051FHeh. Got an itch to explore the tower?\x02\x03",

            "Ah, screw it.\x01",
            "If you want to poke around, I'm in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2644")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2644")

    ChrTalk(    #88
        0x103,
        (
            "#027FAhhhh. Someone's got a bit of a dungeon-\x01",
            "diving itch in her new jacket, I think.\x02\x03",

            "I'll keep an eye on you if you want\x01",
            "to explore the tower, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2644")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Head Back\x01",              # 0
            "Go Dungeon Diving\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2814")

    ChrTalk(    #89
        0x101,
        (
            "#1007F#6PWellll...no, we shouldn't.\x02\x03",

            "Settling up this job's got to come first.\x01",
            "Sadly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2754")

    ChrTalk(    #90
        0x106,
        (
            "#053FAfraid that's how it works.\x02\x03",

            "#050FLet's get back to town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B3")

    label("loc_2754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_27B3")

    ChrTalk(    #91
        0x103,
        (
            "#020FYes, that's a good point for a\x01",
            "bracer to keep in mind.\x02\x03",

            "Let's return to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27F0")

    ChrTalk(    #92
        0x104,
        "#031FLet us away, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x127,
        "#151FYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2808")

    label("loc_27F0")


    ChrTalk(    #94
        0x101,
        "#1006F#6PLet's go.\x02",
    )

    CloseMessageWindow()

    label("loc_2808")

    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A10")

    label("loc_2814")


    ChrTalk(    #95
        0x101,
        (
            "#1006F#6PYeah. I do kinda want to explore it!\x02\x03",

            "I mean, there's a lot of pretty strong monsters\x01",
            "in there, right? It'll be good practice.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2920")

    ChrTalk(    #96
        0x106,
        (
            "#053FI could do with a workout, I guess.\x02\x03",

            "#051FWe'll bash a few monsters and\x01",
            "then head back to town, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BB")

    label("loc_2920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_29BB")

    ChrTalk(    #97
        0x103,
        (
            "#021FWell, I suppose the inhabitants\x01",
            "would make for a nice little workout.\x02\x03",

            "#020FLet's look around a bit, and then\x01",
            "get back as soon as we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29F8")

    ChrTalk(    #98
        0x104,
        "#031FLet us away, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x127,
        "#151FYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_29F8")


    ChrTalk(    #100
        0x101,
        "#1006F#6PIn we go!\x02",
    )

    CloseMessageWindow()

    label("loc_2A10")

    Return()

    # Function_13_230B end

    def Function_14_2A11(): pass

    label("Function_14_2A11")

    OP_62(0x127, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)
    OP_94(0x1, 0x127, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(800)
    OP_94(0x1, 0x127, 0x10E, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    OP_94(0x1, 0x127, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(400)
    OP_94(0x1, 0x127, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(800)
    OP_63(0x127)
    Return()

    # Function_14_2A11 end

    def Function_15_2A7C(): pass

    label("Function_15_2A7C")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AAB")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AC7")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AE3")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2AE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AFF")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2AFF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B1B")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B37")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2B37")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B53")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2B53")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B6F")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2B6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B89")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2B89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BA3")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BBD")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2BBD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD7")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2BD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BF1")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2BF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C0B")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C22")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C22")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C22")

    Return()

    # Function_15_2A7C end

    SaveToFile()

Try(main)
