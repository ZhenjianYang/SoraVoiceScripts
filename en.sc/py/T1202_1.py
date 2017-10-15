from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1202_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1202_1 ._SN',
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
        "Function_1_BD2",          # 01, 1
        "Function_2_C0E",          # 02, 2
        "Function_3_C46",          # 03, 3
        "Function_4_C7E",          # 04, 4
        "Function_5_CB6",          # 05, 5
        "Function_6_CEE",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x46, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -1350, 0, 6540, 0)
    SetChrPos(0x101, -1550, 0, 5470, 0)
    SetChrPos(0xF7, -2700, 0, 5320, 0)
    SetChrPos(0xF8, -1170, 0, 4200, 0)
    SetChrPos(0xF9, -2410, 0, 3740, 0)
    OP_43(0x16, 0x0, 0x1, 0x1)
    Sleep(100)
    OP_43(0x101, 0x0, 0x1, 0x2)
    Sleep(100)
    OP_43(0xF7, 0x0, 0x1, 0x3)
    Sleep(100)
    OP_43(0xF8, 0x0, 0x1, 0x4)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x1, 0x5)
    OP_6D(-1980, 0, 8520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)

    def lambda_18D():
        OP_6D(-1190, 0, 12330, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_1B3():
        OP_6D(21820, -4000, 13880, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B3)

    def lambda_1CB():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CB)

    def lambda_1DB():
        OP_67(0, 8990, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DB)
    WaitChrThread(0x101, 0x3)

    def lambda_1F8():
        OP_6C(0, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F8)
    OP_6B(4000, 4000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Fade(1000)
    OP_44(0x101, 0x3)
    SetChrPos(0x16, 8570, 0, 9930, 90)
    SetChrPos(0x101, 6990, 0, 9850, 92)
    SetChrPos(0xF7, 6630, 0, 11050, 96)
    SetChrPos(0xF8, 6210, 0, 9160, 89)
    SetChrPos(0xF9, 5490, 0, 10320, 93)
    OP_6D(6600, 0, 10880, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x16,
        "#6PSo it's exactly as I'd heard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x16,
        (
            "#6PThey've already started to rebuild their\x01",
            "orchards, little by little.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CA")

    ChrTalk(    #2
        0x109,
        (
            "#1060FYeah, looks like it.\x02\x03",

            "It'll be a hard road for them, but the\x01",
            "journey of a thousand selge begins\x01",
            "with a single step.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E")

    label("loc_3CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449")

    ChrTalk(    #3
        0x106,
        (
            "#051FWe ain't gonna get it all back in a day,\x01",
            "but they're going in the right direction,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E")

    label("loc_449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D0")

    ChrTalk(    #4
        0x103,
        (
            "#020FWell, they'll certainly have their work\x01",
            "cut out for them, but they're taking a\x01",
            "step in the right direction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E")

    label("loc_4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_586")

    ChrTalk(    #5
        0x108,
        (
            "#070FThe road ahead of them will be hard,\x01",
            "but it is good they've taken the first step.\x02\x03",

            "The journey of a thousand selge begins\x01",
            "with a single step, as they say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E")

    label("loc_586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E")

    ChrTalk(    #6
        0x104,
        (
            "#030FThe road before them is treacherous,\x01",
            "but this first step is the most important.\x02\x03",

            "No matter how rough the fields, no fruit\x01",
            "shall grow should no one ever sow it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E")


    ChrTalk(    #7
        0x101,
        (
            "#1000FYeah, they're getting all kinds of help\x01",
            "from all over, too.\x02\x03",

            "I'm sure they'll be just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x16,
        "#6PYes, I believe in them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x16,
        (
            "#6PI wish we merchants could be of some\x01",
            "aid to them...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #10
        0x101,
        (
            "#1011FHuh?\x02\x03",

            "Mirano, are you thinking of trying\x01",
            "to save Ravennue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x16,
        (
            "#6POh, my, no. I have no intention\x01",
            "of setting myself up as some kind\x01",
            "of savior to these people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x16,
        "#6PI'm ultimately just here for business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x16,
        (
            "#6PI'm going to look at the orchards and\x01",
            "get a feel for how bad the situation is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x16,
        (
            "#6POf course, if things are looking up,\x01",
            "I can always invest!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 270, 400)

    ChrTalk(    #15
        0x16,
        "Well, then! I should be getting to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006FOkay!\x02\x03",

            "That means this is goodbye, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        "It is, indeed.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92D")
    OP_28(0x7C, 0x1, 0x10)
    OP_2B(0x7C, 0x2)
    OP_2C(0x7C, 0x1388)

    label("loc_92D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_A04")

    ChrTalk(    #18
        0x16,
        (
            "I must declare, I sorely misjudged you\x01",
            "earlier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        (
            "I'll contact Lugran and arrange a bonus\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1004FHuh? Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x16,
        "Why would I lie about a thing like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x16,
        "You've earned it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A76")

    label("loc_A04")


    ChrTalk(    #23
        0x16,
        "Well, you did well enough, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        (
            "Not quite bonus material, if I do say so\x01",
            "myself, but well enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A76")


    ChrTalk(    #25
        0x16,
        "Be careful on your way back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006FWe will be. Good luck with your work!\x02",
    )

    CloseMessageWindow()

    def lambda_ACF():

        label("loc_ACF")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_ACF")

    QueueWorkItem2(0x0, 1, lambda_ACF)

    def lambda_AE0():

        label("loc_AE0")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AE0")

    QueueWorkItem2(0x1, 1, lambda_AE0)

    def lambda_AF1():

        label("loc_AF1")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AF1")

    QueueWorkItem2(0x2, 1, lambda_AF1)

    def lambda_B02():

        label("loc_B02")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_B02")

    QueueWorkItem2(0x3, 1, lambda_B02)
    OP_43(0x16, 0x0, 0x1, 0x6)
    OP_6D(4800, 0, 14700, 3000)
    Sleep(1000)
    OP_6D(6600, 0, 10880, 2500)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #27
        "Quest #2C[Merchant Escort] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    OP_28(0x7C, 0x1, 0x8)
    OP_28(0x7C, 0x4, 0x10)
    OP_44(0x16, 0x0)
    SetChrPos(0x16, 25990, -4000, 14870, 270)
    OP_43(0x16, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_BD2(): pass

    label("Function_1_BD2")

    OP_8E(0x16, 0xFFFFFABA, 0x0, 0x33AE, 0x7D0, 0x0)
    OP_8C(0x16, 180, 400)
    Sleep(1000)
    OP_8C(0x16, 90, 400)
    Sleep(1000)
    OP_94(0x1, 0x16, 0xF, 0xFA0, 0x7D0, 0x0)
    Return()

    # Function_1_BD2 end

    def Function_2_C0E(): pass

    label("Function_2_C0E")

    OP_8E(0x101, 0xFFFFF9F2, 0x0, 0x2D3C, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0x101, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_2_C0E end

    def Function_3_C46(): pass

    label("Function_3_C46")

    OP_8E(0xF7, 0xFFFFF574, 0x0, 0x2BB6, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF7, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0xF7, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_3_C46 end

    def Function_4_C7E(): pass

    label("Function_4_C7E")

    OP_8E(0xF8, 0xFFFFFB6E, 0x0, 0x2936, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF8, 90, 400)
    Sleep(2000)
    OP_A6(0xC)
    OP_94(0x1, 0xF8, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_4_C7E end

    def Function_5_CB6(): pass

    label("Function_5_CB6")

    OP_8E(0xF9, 0xFFFFF696, 0x0, 0x2738, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xF9, 90, 400)
    Sleep(2000)
    OP_A2(0xC)
    OP_94(0x1, 0xF9, 0x0, 0xBB8, 0x7D0, 0x0)
    Return()

    # Function_5_CB6 end

    def Function_6_CEE(): pass

    label("Function_6_CEE")

    OP_8E(0x16, 0x1662, 0x0, 0x3656, 0x7D0, 0x0)
    OP_8E(0x16, 0x104, 0x0, 0x6E3C, 0x7D0, 0x0)
    Return()

    # Function_6_CEE end

    SaveToFile()

Try(main)
