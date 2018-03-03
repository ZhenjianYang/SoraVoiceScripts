from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2219   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2219.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2219   ._SN',
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
        'Vogt',                                 # 9
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


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
    )

    DeclNpc(
        X                   = -2870,
        Z                   = 0,
        Y                   = 202000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_D3",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_25A",          # 03, 3
        "Function_4_AEC",          # 04, 4
        "Function_5_B4D",          # 05, 5
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Return()

    # Function_0_D2 end

    def Function_1_D3(): pass

    label("Function_1_D3")

    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x5)
    Return()

    # Function_1_D3 end

    def Function_2_DD(): pass

    label("Function_2_DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_244")

    label("loc_102")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_244")

    label("loc_11B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_244")

    label("loc_134")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_244")

    label("loc_14D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_244")

    label("loc_166")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_244")

    label("loc_17F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_244")

    label("loc_198")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_244")

    label("loc_1B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_244")

    label("loc_1CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_244")

    label("loc_1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_244")

    label("loc_1FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_244")

    label("loc_215")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_244")

    label("loc_22E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_259")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_244")

    label("loc_259")

    Return()

    # Function_2_DD end

    def Function_3_25A(): pass

    label("Function_3_25A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_34F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B2")

    ChrTalk(    #0
        0xFE,
        (
            "I reckon my happiness is right here in this\x01",
            "lighthouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C")

    label("loc_2B2")


    ChrTalk(    #1
        0xFE,
        (
            "There's actually a shining stone here in this\x01",
            "lighthouse, though, even if it's not what you\x01",
            "are looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "I reckon that's my happiness...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_34C")

    Jump("loc_6C1")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 4)), scpexpr(EXPR_END)), "loc_477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3DF")

    ChrTalk(    #3
        0xFE,
        (
            "There's no shame in relying on others for\x01",
            "help if you need it! Grab 'em by the collar\x01",
            "and scream for help if you need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_474")

    label("loc_3DF")


    ChrTalk(    #4
        0xFE,
        "You lookin' for some help, young lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "What do you need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x14E,
        (
            "#1714FN-No. I'll be fine, honestly...\x02\x03",

            "#1713FThank you for offering, sir.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_474")

    Jump("loc_6C1")

    label("loc_477")

    EventBegin(0x1)
    OP_8C(0xFE, 270, 0)
    Fade(1000)
    OP_6D(-1600, 0, 202380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x14E, -1280, 0, 202300, 270)
    Sleep(1000)

    ChrTalk(    #7
        0xFE,
        (
            "I swear, this is EXACTLY what's wrong\x01",
            "with youngins these days...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 90, 500)
    Sleep(500)

    ChrTalk(    #8
        0xFE,
        "Wh-What are you doing here, young lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14E,
        (
            "#1712FU-Umm... Excuse me, sir...\x02\x03",

            "You haven't seen a young girl other\x01",
            "than me in here recently have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "A young girl? 'Fraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x14E,
        (
            "#1713FI-I see...\x02\x03",

            "Sorry for troubling you...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_639():

        label("loc_639")

        TurnDirection(0xFE, 0x14E, 0)
        OP_48()
        Jump("loc_639")

    QueueWorkItem2(0x10, 3, lambda_639)
    OP_43(0x14E, 0x3, 0x0, 0x4)
    Sleep(3000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #12
        0xFE,
        "I swear, kids these days...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "They sure are a pain.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F44)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x3)
    NewScene("ED6_DT21/C2219   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_6C1")

    Jump("loc_AE8")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_721")

    ChrTalk(    #14
        0xFE,
        "A happiness stone, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "You think somethin' like that exists?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADE")

    label("loc_721")

    EventBegin(0x1)
    OP_8C(0xFE, 270, 0)
    Fade(1000)
    OP_6D(-1600, 0, 202380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x14E, -1250, 0, 202480, 270)
    SetChrPos(0x14F, -1060, 0, 201620, 270)
    Sleep(1000)

    ChrTalk(    #16
        0xFE,
        "I swear, kids these days...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 90, 500)
    Sleep(500)

    ChrTalk(    #17
        0xFE,
        "Wh-What might you two be doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14E,
        "#1718FHello!\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_63(0x14E)

    ChrTalk(    #19
        0x14E,
        (
            "#1714FActually, lighthouses are pretty high up,\x01",
            "aren't they?\x02\x03",

            "#1718FSir, you haven't seen a happiness stone before,\x01",
            "have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "A-A happiness stone?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14F,
        "#1730FThey're really shiny and pretty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "N-No, I don't recall ever seein' any\x01",
            "such thing in all my years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1716FOh... That's too bad...\x02\x03",

            "#1710FWell, thank you, anyway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    Sleep(400)

    ChrTalk(    #24
        0x14E,
        "#1718FLet's keep looking, Polly! \x02",
    )

    CloseMessageWindow()
    OP_43(0x14E, 0x3, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #25
        0x14F,
        "#1731FI hope your back feels better, mister!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A1A():

        label("loc_A1A")

        TurnDirection(0xFE, 0x14F, 0)
        OP_48()
        Jump("loc_A1A")

    QueueWorkItem2(0x10, 3, lambda_A1A)
    OP_43(0x14F, 0x3, 0x0, 0x4)
    Sleep(3000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #26
        0xFE,
        "I swear, kids these days...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "...They're sharp little devils, aren't they?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0xFE,
        "A happiness stone, hmm...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F43)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x3)
    NewScene("ED6_DT21/C2219   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_ADE")

    Jump("loc_AE8")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_AE8")

    label("loc_AE8")

    TalkEnd(0xFE)
    Return()

    # Function_3_25A end

    def Function_4_AEC(): pass

    label("Function_4_AEC")


    def lambda_AF2():
        OP_8E(0xFE, 0xB04, 0x0, 0x32104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF2)
    WaitChrThread(0xFE, 0x1)

    def lambda_B12():
        OP_8E(0xFE, 0xB04, 0x0, 0x3283E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B12)
    WaitChrThread(0xFE, 0x1)

    def lambda_B32():
        OP_8E(0xFE, 0xFFFFF254, 0xFFFFF830, 0x328F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B32)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_AEC end

    def Function_5_B4D(): pass

    label("Function_5_B4D")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_5_B4D end

    SaveToFile()

Try(main)
