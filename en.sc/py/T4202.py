from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Queen Alicia',                         # 9
        'Sieg',                                 # 10
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02323 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02323P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 2090,
        TriggerZ            = 12000,
        TriggerY            = 67030,
        TriggerRange        = 1000,
        ActorX              = 5244,
        ActorZ              = -10900,
        ActorY              = 81768,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1920,
        TriggerZ            = 12000,
        TriggerY            = 58790,
        TriggerRange        = 4700,
        ActorX              = 1920,
        ActorZ              = 12000,
        ActorY              = 60790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1EC",          # 02, 2
        "Function_3_202",          # 03, 3
        "Function_4_853",          # 04, 4
        "Function_5_D30",          # 05, 5
        "Function_6_D6D",          # 06, 6
        "Function_7_DAA",          # 07, 7
        "Function_8_DE7",          # 08, 8
        "Function_9_E24",          # 09, 9
        "Function_10_E39",         # 0A, 10
        "Function_11_E4E",         # 0B, 11
        "Function_12_E63",         # 0C, 12
        "Function_13_E78",         # 0D, 13
        "Function_14_F82",         # 0E, 14
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_14C")
    Jump("loc_173")

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_156")
    Jump("loc_173")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_173")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1800, 12000, 67020, 0)

    label("loc_173")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_17F"),
        (SWITCH_DEFAULT, "loc_197"),
    )


    label("loc_17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_194")

    Jump("loc_197")

    label("loc_197")

    Return()

    # Function_0_142 end

    def Function_1_198(): pass

    label("Function_1_198")

    OP_E8(0x88, 0x13, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0")
    OP_82(0x80, 0x0)
    OP_64(0x0, 0x1)

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D6")
    OP_B1("t4202_y")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jump("loc_1DF")

    label("loc_1D6")

    OP_B1("t4202_n")

    label("loc_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB")
    OP_64(0x1, 0x1)

    label("loc_1EB")

    Return()

    # Function_1_198 end

    def Function_2_1EC(): pass

    label("Function_2_1EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_201")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1EC")

    label("loc_201")

    Return()

    # Function_2_1EC end

    def Function_3_202(): pass

    label("Function_3_202")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E6")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        (
            "#097FWhy, Klaudia and Estelle!\x02\x03",

            "#090FI've already received a report\x01",
            "about Kanone's deeds from\x01",
            "Julia.\x02\x03",

            "Though truly, she was a problem\x01",
            "I should have solved personally.\x02\x03",

            "Estelle, everyone, I am so very\x01",
            "sorry for this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1025FN-No, not at all...\x02\x03",

            "#1000FBesides, Renne... The one behind\x01",
            "this isn't a total stranger to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#094FYes, I'd heard.\x02\x03",

            "#092FFor a small child like that to be a member of the\x01",
            "society was, frankly, a shock.\x02\x03",

            "Her and the existence of her giant orbal construct\x01",
            "could cause confusion amongst the citizenry,\x01",
            "so I'm considering keeping it a secret for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4BE")

    ChrTalk(    #3
        0x106,
        (
            "#050FIt's a bit frustratin',\x01",
            "but probably for the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC")

    label("loc_4BE")


    ChrTalk(    #4
        0x103,
        (
            "#020FIt is frustrating, but it's \x01",
            "probably for the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC")


    ChrTalk(    #5
        0x105,
        (
            "#042FYes, depending on the situation,\x01",
            "it could even cause significant\x01",
            "effects internationally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1004FI-It'd go that far?\x02\x03",

            "#1009FYeah, next time I meet Renne,\x01",
            "she is soooo getting a spanking\x01",
            "for this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#094FYou may leave searching for\x01",
            "them to Cassius and General\x01",
            "Morgan.\x02\x03",

            "I intend to do everything I can\x01",
            "on my end as well.\x02\x03",

            "#090FFor now, that means I must see\x01",
            "the signing ceremony through safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000FI know you'll see it through,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#090FEstelle, I know it won't be easy,\x01",
            "but I need you to stay strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1018FOf course!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #11
        0x8,
        "#094FAnd...Klaudia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#040F...Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#090FI look forward to hearing your\x01",
            "answer soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#042FYes, Grandmother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "#090FWell, then... Everyone, take care.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1651)
    Jump("loc_84F")

    label("loc_7E6")


    ChrTalk(    #16
        0x8,
        (
            "#090FEstelle, I know it won't be easy,\x01",
            "but I need you to stay strong.\x02\x03",

            "Please take care of Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F")

    TalkEnd(0x8)
    Return()

    # Function_3_202 end

    def Function_4_853(): pass

    label("Function_4_853")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 2000, 12000, 67000, 180)
    SetChrPos(0x9, 1110, 12500, 67800, 180)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_6D(2480, 12000, 54000, 0)
    OP_67(0, 10780, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x108, 0x1, 0x0, 0x8)
    Sleep(100)
    OP_43(0x104, 0x1, 0x0, 0x7)
    FadeToBright(2000, 0)
    WaitChrThread(0x108, 0x1)
    OP_0D()

    NpcTalk(    #17
        0x8,
        "Elderly Woman's Voice",
        "Ah, you've finally arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1004F#7PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#044F#6PGrandmother?\x02",
    )

    CloseMessageWindow()

    def lambda_97A():
        OP_6D(2130, 12000, 66280, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97A)

    def lambda_992():
        OP_67(0, 6260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_992)

    def lambda_9AA():
        OP_6B(2610, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9AA)

    def lambda_9BA():
        OP_6E(279, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_9BA)
    Sleep(1500)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_43(0x105, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0x108, 0x0, 0x0, 0xC)
    Sleep(100)
    OP_43(0x104, 0x0, 0x0, 0xB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #20
        0x9,
        "#311F#3PScreee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1004F#4PBwuh, Sieg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        (
            "#047F#4PI see...\x02\x03",

            "#048FHaha. Sieg was being thoughtful,\x01",
            "wasn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#091F#6PYes, he let me know you were\x01",
            "coming.\x02\x03",

            "#090FWelcome home, Klaudia.\x02\x03",

            "And Estelle! You are always\x01",
            "welcome so long as I remain Queen.\x02\x03",

            "#094FYour father explained everything,\x01",
            "not long after you left to train.\x02\x03",

            "It pains me to know you carry\x01",
            "such a burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1026F#4POh...\x02\x03",

            "#1016FUm, ah, thank you very much,\x01",
            "Your Majesty.\x02\x03",

            "#1006FStill, I know what I gotta do,\x01",
            "and Kloe's been a huge help!\x02\x03",

            "So I'm okay. Don't worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#094F#6PHm. I see...\x02\x03",

            "#090FYour soul has gained new steel\x01",
            "since we met last, Estelle.\x02\x03",

            "Mr. Vathek and...Mr. Lenheim.\x01",
            "Both of you, of course, are also\x01",
            "welcome in my home.\x02\x03",

            "#091FLet us retire to my chambers.\x01",
            "I shall have some tea prepared.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4230   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_4_853 end

    def Function_5_D30(): pass

    label("Function_5_D30")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2740, 12000, 49900, 0)

    def lambda_D4C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D4C)
    OP_8E(0xFE, 0xA3C, 0x2EE0, 0xD2F0, 0x7D0, 0x0)
    Return()

    # Function_5_D30 end

    def Function_6_D6D(): pass

    label("Function_6_D6D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1630, 12000, 49890, 0)

    def lambda_D89():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D89)
    OP_8E(0xFE, 0x65E, 0x2EE0, 0xD2F0, 0x7D0, 0x0)
    Return()

    # Function_6_D6D end

    def Function_7_DAA(): pass

    label("Function_7_DAA")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1650, 12000, 49050, 0)

    def lambda_DC6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC6)
    OP_8E(0xFE, 0x636, 0x2EE0, 0xCEA4, 0x7D0, 0x0)
    Return()

    # Function_7_DAA end

    def Function_8_DE7(): pass

    label("Function_8_DE7")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2730, 12000, 49060, 0)

    def lambda_E03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E03)
    OP_8E(0xFE, 0xA3C, 0x2EE0, 0xCEA4, 0x7D0, 0x0)
    Return()

    # Function_8_DE7 end

    def Function_9_E24(): pass

    label("Function_9_E24")

    OP_8E(0xFE, 0x9C4, 0x2EE0, 0xFE4B, 0xBB8, 0x0)
    Return()

    # Function_9_E24 end

    def Function_10_E39(): pass

    label("Function_10_E39")

    OP_8E(0xFE, 0x528, 0x2EE0, 0xFE4B, 0xBB8, 0x0)
    Return()

    # Function_10_E39 end

    def Function_11_E4E(): pass

    label("Function_11_E4E")

    OP_8E(0xFE, 0x4D8, 0x2EE0, 0xF8F2, 0xBB8, 0x0)
    Return()

    # Function_11_E4E end

    def Function_12_E63(): pass

    label("Function_12_E63")

    OP_8E(0xFE, 0x992, 0x2EE0, 0xF8CA, 0xBB8, 0x0)
    Return()

    # Function_12_E63 end

    def Function_13_E78(): pass

    label("Function_13_E78")

    EventBegin(0x1)

    ChrTalk(    #26
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_EA4():
        OP_6D(-2750, 12000, 67810, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EA4)

    def lambda_EBC():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EBC)

    def lambda_ECC():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_ECC)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F72")
    OP_C0(0xE, 0x2E, 0x852, 0x2EE0, 0x105D6, 0x168, 0x147C, 0xFFFFD56C, 0x13F68)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_F81")

    label("loc_F72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F81")
    EventEnd(0x1)

    label("loc_F81")

    Return()

    # Function_13_E78 end

    def Function_14_F82(): pass

    label("Function_14_F82")

    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CE, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_14_F82 end

    SaveToFile()

Try(main)
