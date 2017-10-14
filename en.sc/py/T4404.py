from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4404   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Duke Dunan',                           # 9
        'Kanone',                               # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Special Ops Soldier',                  # 17
        'Orgueille',                            # 18
        'Grancel Harbor',                       # 19
        'アタックドーベン',                     # 20
        'アタックドーベン',                     # 21
        'アタックドーベン',                     # 22
        'アタックドーベン',                     # 23
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
        'ED6_DT07/CH02140 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH01330 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00121 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT27/CH04080 ._CH',             # 09
        'ED6_DT27/CH04081 ._CH',             # 0A
        'ED6_DT07/CH00340 ._CH',             # 0B
        'ED6_DT07/CH00341 ._CH',             # 0C
        'ED6_DT07/CH00344 ._CH',             # 0D
        'ED6_DT07/CH00440 ._CH',             # 0E
        'ED6_DT07/CH00441 ._CH',             # 0F
        'ED6_DT07/CH00441 ._CH',             # 10
        'ED6_DT07/CH00444 ._CH',             # 11
        'ED6_DT09/CH10060 ._CH',             # 12
        'ED6_DT09/CH10061 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02140P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH01330P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00121P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT27/CH04080P._CP',             # 09
        'ED6_DT27/CH04081P._CP',             # 0A
        'ED6_DT07/CH00340P._CP',             # 0B
        'ED6_DT07/CH00341P._CP',             # 0C
        'ED6_DT07/CH00344P._CP',             # 0D
        'ED6_DT07/CH00440P._CP',             # 0E
        'ED6_DT07/CH00441P._CP',             # 0F
        'ED6_DT07/CH00441P._CP',             # 10
        'ED6_DT07/CH00444P._CP',             # 11
        'ED6_DT09/CH10060P._CP',             # 12
        'ED6_DT09/CH10061P._CP',             # 13
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -880,
        Z                   = 0,
        Y                   = -32689,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -670,
        Z                   = 0,
        Y                   = 15150,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11530,
        Z                   = 0,
        Y                   = 35690,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13160,
        Z                   = 0,
        Y                   = 25810,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14350,
        Z                   = 0,
        Y                   = 44170,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 21200,
        Y                   = -2000,
        Z                   = 47800,
        Range               = 23000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xF35C,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_33A",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_3F1",          # 02, 2
        "Function_3_407",          # 03, 3
        "Function_4_1111",         # 04, 4
        "Function_5_1137",         # 05, 5
        "Function_6_115D",         # 06, 6
        "Function_7_1183",         # 07, 7
        "Function_8_11CA",         # 08, 8
        "Function_9_11F0",         # 09, 9
        "Function_10_1216",        # 0A, 10
        "Function_11_1241",        # 0B, 11
        "Function_12_1267",        # 0C, 12
        "Function_13_28D7",        # 0D, 13
        "Function_14_2919",        # 0E, 14
        "Function_15_296F",        # 0F, 15
        "Function_16_29C0",        # 10, 16
        "Function_17_2A16",        # 11, 17
        "Function_18_2A4D",        # 12, 18
        "Function_19_2A76",        # 13, 19
        "Function_20_2A9F",        # 14, 20
    )


    def Function_0_33A(): pass

    label("Function_0_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35A")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_35A")

    Return()

    # Function_0_33A end

    def Function_1_35B(): pass

    label("Function_1_35B")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x45D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_387")

    OP_72(0x7, 0x10)
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0x7, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x8, 0x10)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x5, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x5, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x6, 0x4)
    OP_71(0xC, 0x4)
    Return()

    # Function_1_35B end

    def Function_2_3F1(): pass

    label("Function_2_3F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_406")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F1")

    label("loc_406")

    Return()

    # Function_2_3F1 end

    def Function_3_407(): pass

    label("Function_3_407")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_423")

    Fade(1000)
    OP_6D(22590, 0, 54310, 0)
    OP_67(0, 12420, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(138000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 22670, 0, 55450, 90)
    SetChrPos(0xF7, 22590, 0, 54260, 90)
    SetChrPos(0x109, 21470, 0, 54830, 90)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x8, 37560, 0, 53580, 270)
    SetChrPos(0x9, 35110, 0, 55020, 270)
    SetChrPos(0xA, 38350, 0, 53580, 270)
    SetChrPos(0xB, 35840, 0, 55950, 270)
    SetChrPos(0xC, 35880, 0, 54180, 270)
    SetChrPos(0xD, 36530, 0, 56690, 270)
    SetChrPos(0xE, 36530, 0, 53240, 270)
    SetChrPos(0xF, 38030, 0, 55680, 270)
    SetChrPos(0x10, 37130, 0, 54760, 270)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    OP_20(0x7D0)

    NpcTalk(    #0
        0x9,
        "Woman's Voice",
        "#4PFinally shown up, have we?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_614():
        OP_6D(33260, 0, 54610, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_614)

    def lambda_62C():
        OP_67(0, 6790, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62C)

    def lambda_644():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_644)

    def lambda_654():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_654)

    def lambda_664():
        OP_6E(316, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_664)

    def lambda_674():
        OP_8E(0xFE, 0x7148, 0x0, 0xD9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_674)
    Sleep(100)

    def lambda_694():
        OP_8E(0xFE, 0x7148, 0x0, 0xD53E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_694)
    Sleep(200)

    def lambda_6B4():
        OP_8E(0xFE, 0x6D4C, 0x0, 0xD818, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B4)
    Sleep(1000)
    OP_1D(0x56)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #1
        0x101,
        "#1005F#2PCaptain Amalthea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#1182F#6PEx-captain, thanks to you.\x02\x03",

            "I thought the dogs were making too much\x01",
            "noise, and when I come out to look...\x02\x03",

            "I suppose bracers ARE rather like dogs,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1005F#2PDon't screw with us!\x01",
            "Hurting our friends, abducting people!\x02\x03",

            "And Renne has nothing to do with this...\x01",
            "You are NOT getting away with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#1181F#6PReally, what ARE you going on about?\x02\x03",

            "I simply wish to help His Highness,\x01",
            "Duke Dunan von Auslese,\x01",
            "take his rightful place on the throne.\x02\x03",

            "It has little to do with you, girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1020F#2PWhat in--?!\x02\x03",

            "DUNAN? You're making the same\x01",
            "dumb mistake again?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        (
            "#226F#6PWh-What kind of idiot would join a\x01",
            "fool's errand like this?!\x02\x03",

            "You have to help me! They intend\x01",
            "to use me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1060FYeah, he seems like a reeeeeeal willing\x01",
            "participant, there, Ms. Amalthea.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A92")

    ChrTalk(    #8
        0x106,
        (
            "#057F#2PC'mon, you old bat. Come clean.\x02\x03",

            "This is really about freein' Richard, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFB")

    label("loc_A92")


    ChrTalk(    #9
        0x103,
        (
            "#022F#2PEnough of the games, Ms. Ex-Captain.\x02\x03",

            "Your real goal is freeing Colonel Richard,\x01",
            "is it not?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFB")


    ChrTalk(    #10
        0x101,
        "#1004F#2P#3SWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#1183F#6PWell, if you've figured that out,\x01",
            "then we can dispense with the\x01",
            "pleasantries.\x02\x03",

            "#1186FEveryone!\x01",
            "Commence Operation Pride's Resurgence!\x02\x03",

            "You men! Hold them off for at least \x01",
            "a few minutes!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Special Ops Soldiers")

    AnonymousTalk(    #12
        "\x07\x00#3SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_C36():
        OP_6D(37020, 0, 54410, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C36)

    def lambda_C4E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C4E)
    OP_43(0xD, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0xF, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0x6)
    SetChrFlags(0x8, 0x20)

    def lambda_C80():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C80)
    Sleep(50)

    def lambda_C93():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C93)
    Sleep(50)

    def lambda_CA6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CA6)

    def lambda_CB4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CB4)
    Sleep(500)

    def lambda_CC7():
        OP_8E(0xFE, 0xBA54, 0x3E8, 0xD67E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CC7)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0xA, 2)

    def lambda_D08():
        OP_8E(0xFE, 0xB66C, 0x3E8, 0xD37C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D08)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_D2F():
        OP_8F(0xFE, 0xB66C, 0x3E8, 0xD37C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D2F)

    def lambda_D4A():

        label("loc_D4A")

        OP_9E(0xFE, 0x1E, 0x0, 0x1F4, 0xBB8)
        OP_48()
        Jump("loc_D4A")

    QueueWorkItem2(0x8, 2, lambda_D4A)
    Sleep(200)
    SetChrChipByIndex(0xB, 15)

    def lambda_D71():
        OP_8E(0xFE, 0xB284, 0x3E8, 0xDA8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D71)
    SetChrChipByIndex(0xC, 12)

    def lambda_D91():
        OP_8E(0xFE, 0xB284, 0x3E8, 0xD3A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D91)

    def lambda_DAC():
        OP_6D(33260, 0, 54610, 1200)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_DAC)
    OP_43(0x9, 0x2, 0x0, 0x7)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #13
        0x101,
        (
            "#1005F#2PHang on a sec!\x02\x03",

            "I don't care about the duke,\x01",
            "but let Renne go, damn it!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0xF, 0x1, 0x0, 0xA)
    OP_43(0x10, 0x1, 0x0, 0xB)

    def lambda_E42():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E42)
    Sleep(100)

    def lambda_E62():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_E62)
    Sleep(100)

    def lambda_E82():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E82)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #14
        0xD,
        "#3PWe won't let you interfere with the plan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        "#6PCome on, you guild dogs!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1005F#2PYou...\x02",
    )

    CloseMessageWindow()
    Fade(400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4C")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 7)
    Jump("loc_F56")

    label("loc_F4C")

    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 5)

    label("loc_F56")

    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #17
        0x106,
        "#054F#2PFine by me! Come get some!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE7")

    label("loc_FA4")


    ChrTalk(    #18
        0x103,
        (
            "#024F#2PHow very brave...\x01",
            "I hope you're ready for punishment!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    Sleep(100)
    SetChrChipByIndex(0xD, 12)
    SetChrChipByIndex(0xE, 12)
    SetChrChipByIndex(0xF, 15)
    SetChrChipByIndex(0x10, 15)

    def lambda_1006():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1006)

    def lambda_1021():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1021)

    def lambda_103C():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_103C)

    def lambda_1057():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1057)

    def lambda_1072():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1072)

    def lambda_108D():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_108D)

    def lambda_10A8():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10A8)

    def lambda_10C3():
        OP_6B(2510, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10C3)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x45D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1107"),
        (SWITCH_DEFAULT, "loc_110C"),
    )


    label("loc_1107")

    OP_B4(0x0)
    Jump("loc_110C")

    label("loc_110C")

    Call(0, 12)
    Return()

    # Function_3_407 end

    def Function_4_1111(): pass

    label("Function_4_1111")

    SetChrChipByIndex(0xFE, 12)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x8F16, 0x0, 0xE254, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_4_1111 end

    def Function_5_1137(): pass

    label("Function_5_1137")

    SetChrChipByIndex(0xFE, 15)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x942A, 0x0, 0xDE44, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_5_1137 end

    def Function_6_115D(): pass

    label("Function_6_115D")

    SetChrChipByIndex(0xFE, 15)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x8FDE, 0x0, 0xDE3A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_6_115D end

    def Function_7_1183(): pass

    label("Function_7_1183")

    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0x8, 0x2)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 45)
    OP_70(0x0, 0x1F)
    OP_22(0xD3, 0x0, 0x64)
    OP_73(0x0)
    Sleep(400)
    OP_22(0x73, 0x0, 0x64)
    Return()

    # Function_7_1183 end

    def Function_8_11CA(): pass

    label("Function_8_11CA")

    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x8BB0, 0x0, 0xD9B2, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_8_11CA end

    def Function_9_11F0(): pass

    label("Function_9_11F0")

    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x8B42, 0x0, 0xD354, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_9_11F0 end

    def Function_10_1216(): pass

    label("Function_10_1216")

    Sleep(100)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x91DC, 0x0, 0xD994, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_10_1216 end

    def Function_11_1241(): pass

    label("Function_11_1241")

    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x90B0, 0x0, 0xD1E2, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_11_1241 end

    def Function_12_1267(): pass

    label("Function_12_1267")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrPos(0x101, 33440, 0, 55730, 90)
    SetChrPos(0xF7, 33440, 0, 54390, 90)
    SetChrPos(0x109, 32000, 0, 55000, 90)
    SetChrPos(0xD, 37250, 0, 55300, 270)
    SetChrPos(0xE, 37250, 0, 54000, 270)
    SetChrPos(0xF, 38260, 0, 55760, 270)
    SetChrPos(0x10, 38260, 0, 53780, 270)
    SetChrChipByIndex(0x101, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131A")
    SetChrChipByIndex(0x106, 7)
    Jump("loc_131F")

    label("loc_131A")

    SetChrChipByIndex(0x103, 5)

    label("loc_131F")

    SetChrChipByIndex(0x109, 9)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xF, 17)
    SetChrChipByIndex(0x10, 17)
    SetChrSubChip(0xD, 3)
    SetChrSubChip(0xE, 3)
    SetChrSubChip(0xF, 3)
    SetChrSubChip(0x10, 3)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_6D(35640, 0, 54600, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(133000, 0)
    OP_6E(316, 0)
    LoadEffect(0x0, "monster\\ms30600d.eff")
    LoadEffect(0x1, "monster\\ms30602a.eff")
    LoadEffect(0x2, "monster\\ms30602b.eff")
    LoadEffect(0x3, "monster\\ms30600b.eff")
    LoadEffect(0x4, "monster\\ms30600a.eff")
    OP_6F(0x0, 31)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0xF,
        "#3PArgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#6PHow the hell are they...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1005F#2PJust GIVE UP already!\x02\x03",

            "C'mon! Out of my way...\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0xC, 0x4)
    OP_A1(0x11, 0xC)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 47700, 1000, 54940, 270)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_20(0x0)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 2)
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1020F#2PWaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        "#1069FWhat in the?!\x02",
    )

    CloseMessageWindow()
    OP_6D(38840, 40, 54260, 1000)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 2)
    OP_70(0x0, 0x4)
    OP_22(0x10F, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x71)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C8")

    ChrTalk(    #24
        0x106,
        (
            "#054F#2PAw, HELL! That must be the thing from\x01",
            "the blueprints!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1704")

    label("loc_16C8")


    ChrTalk(    #25
        0x103,
        (
            "#024F#2PThat has to be the device\x01",
            "from the blueprints!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1704")


    ChrTalk(    #26
        0xF,
        (
            "#5PHah...haha...\x01",
            "Looks like we bought enough time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "#2PLong live Colonel Richard's dream...!\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 4)
    OP_70(0x0, 0x1D)
    Sleep(500)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x1E)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x1E)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x1E)

    def lambda_182F():
        OP_96(0xFE, 0x8110, 0x0, 0xD9B2, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_182F)

    def lambda_184D():
        OP_96(0xFE, 0x8110, 0x0, 0xD476, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_184D)

    def lambda_186B():
        OP_96(0xFE, 0x7B70, 0x0, 0xD6D8, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_186B)
    Sleep(500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #28
        0x101,
        "#1014FAieeee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        "#1070FThe heck...?\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x3, 0x3, 0x11, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1932():
        OP_6D(40070, 1000, 54760, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1932)

    def lambda_194A():
        OP_67(0, 2600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_194A)

    def lambda_1962():
        OP_6B(4190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1962)

    def lambda_1972():
        OP_6C(90000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1972)

    def lambda_1982():
        OP_6E(243, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1982)
    OP_43(0xD, 0x1, 0x0, 0xD)
    OP_43(0xE, 0x1, 0x0, 0xE)
    OP_43(0xF, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x1, 0x0, 0x10)
    OP_24(0x75, 0x64)

    def lambda_19B2():

        label("loc_19B2")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_19B2")

    QueueWorkItem2(0x11, 3, lambda_19B2)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0xC, 0x20)
    OP_B0(0xC, 0xF)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)
    Sleep(300)

    def lambda_1A53():
        OP_8E(0x11, 0xA028, 0x3E8, 0xD69C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A53)
    OP_22(0x110, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x5, 0x11, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x11, 0x1)
    OP_23(0x110)
    OP_44(0x11, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x14)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #30
        0x101,
        "#1020F#5PA...TANK?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(    #31
        0x106,
        "#057F#2PThis is the 'Orgueille,' then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B82")

    label("loc_1B57")


    ChrTalk(    #32
        0x103,
        "#022F#2PThe 'Orgueille,' I presume...\x02",
    )

    CloseMessageWindow()

    label("loc_1B82")

    OP_B0(0xC, 0xF)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)

    def lambda_1B9A():

        label("loc_1B9A")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1B9A")

    QueueWorkItem2(0x11, 3, lambda_1B9A)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_1C24():
        OP_8E(0x11, 0x8944, 0x0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C24)
    OP_22(0x110, 0x0, 0x64)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_1C4E():
        OP_96(0xFE, 0x5DAC, 0x0, 0xD6EC, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C4E)
    Sleep(50)

    def lambda_1C71():
        OP_96(0xFE, 0x61BC, 0x0, 0xD412, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1C71)
    Sleep(50)

    def lambda_1C94():
        OP_96(0xFE, 0x61C6, 0x0, 0xD926, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C94)
    Sleep(50)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x11, 0x1)
    OP_23(0x110)
    OP_44(0x11, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x14)
    Fade(1000)
    OP_6D(31230, 0, 53830, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(135000, 0)
    OP_6E(538, 0)
    OP_0D()
    OP_72(0xC, 0x20)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0xC, 371)
    OP_70(0xC, 0x186)
    OP_73(0xC)
    OP_73(0xC)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 35050, 2000, 56100, 270)

    def lambda_1D77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1D77)
    OP_8F(0x9, 0x88EA, 0xA28, 0xDB24, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        (
            "#1181F#6PWell, then...\x01",
            "Do you like our little Orgueille?\x02\x03",

            "This is a high-speed tank we in the\x01",
            "Intelligence Division have been developing\x01",
            "for a while now.\x02\x03",

            "Twice the firepower of the little tin\x01",
            "cans the Empire uses...and more than\x01",
            "a match for one of our airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1068F#2PThaaaat's not gonna be too easy\x01",
            "to take on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1009F#2PThis is...crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#1181F#6PWe never could find the proper engine\x01",
            "to run it, so we stored it away just shy\x01",
            "of completion.\x02\x03",

            "But the engine from the Arseille has\x01",
            "proven to be just what we needed.\x02\x03",

            "Ah, She Who Dwells Above is smiling\x01",
            "on our cause today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1005F#2PW-Wait...\x02\x03",

            "What're you planning on doing with\x01",
            "that thing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#1181F#6PWeren't you listening?\x01",
            "I'm taking the duke to his rightful\x01",
            "throne as king.\x02\x03",

            "I'll have to get the queen to...acquiesce,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1020F#2PNo way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_211F")

    ChrTalk(    #40
        0x106,
        "#054F#2PYou're attacking the CASTLE?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_214A")

    label("loc_211F")


    ChrTalk(    #41
        0x103,
        "#024F#2PYou're attacking the CASTLE?!\x02",
    )

    CloseMessageWindow()

    label("loc_214A")


    ChrTalk(    #42
        0x9,
        (
            "#1188F#6PHAHA! A little slow on the uptake,\x01",
            "bracers!\x02\x03",

            "The Orgueille will put an end to the\x01",
            "legend of Grancel Castle's invincibility\x01",
            "with barely an effort!\x02\x03",

            "And the pathetic guard forces on duty\x01",
            "cannot hope to stop us!\x02\x03",

            "Find some seats!\x01",
            "Tonight the reign of Alicia ends!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2263():
        OP_69(0x11, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2263)
    OP_8F(0x9, 0x88EA, 0x7D0, 0xDB24, 0x7D0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0x9, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0xC, 391)
    OP_70(0xC, 0x19A)
    OP_73(0xC)

    def lambda_22AB():

        label("loc_22AB")

        OP_69(0x11, 0x0)
        OP_48()
        Jump("loc_22AB")

    QueueWorkItem2(0x11, 1, lambda_22AB)
    OP_B0(0xC, 0xF)
    OP_71(0xC, 0x20)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)

    def lambda_22D3():

        label("loc_22D3")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_22D3")

    QueueWorkItem2(0x11, 3, lambda_22D3)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8E(0x11, 0x7E0E, 0x0, 0xD5D4, 0x7D0, 0x0)

    def lambda_2371():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2371)

    def lambda_2381():
        OP_8E(0xFE, 0x53CA, 0x0, 0xD5D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2381)
    OP_22(0x110, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_23DC():
        OP_96(0xFE, 0x6482, 0x0, 0xE7F4, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23DC)
    Sleep(50)

    def lambda_23FF():
        OP_96(0xFE, 0x6446, 0x0, 0xC576, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_23FF)
    Sleep(50)

    def lambda_2422():
        OP_96(0xFE, 0x5D70, 0x0, 0xE772, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2422)

    def lambda_2440():

        label("loc_2440")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2440")

    QueueWorkItem2(0x101, 3, lambda_2440)

    def lambda_2451():

        label("loc_2451")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2451")

    QueueWorkItem2(0xF7, 2, lambda_2451)

    def lambda_2462():

        label("loc_2462")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2462")

    QueueWorkItem2(0x109, 2, lambda_2462)
    WaitChrThread(0x11, 0x2)
    OP_43(0x11, 0x2, 0x0, 0x11)

    def lambda_247F():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_247F)
    OP_6F(0xC, 61)
    OP_70(0xC, 0x50)
    OP_22(0x1FE, 0x0, 0x64)
    Sleep(100)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x1E)
    OP_6F(0x8, 1)
    OP_70(0x8, 0x1E)
    Sleep(10)
    OP_6F(0x2, 1)
    OP_70(0x2, 0x1E)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x1E)
    OP_44(0x11, 0x1)

    def lambda_24E6():

        label("loc_24E6")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_24E6")

    QueueWorkItem2(0x11, 0, lambda_24E6)
    Sleep(4000)
    OP_24(0x10F, 0x5A)
    OP_24(0x110, 0x5A)
    Sleep(100)
    OP_24(0x10F, 0x50)
    OP_24(0x110, 0x50)
    Sleep(100)
    OP_24(0x10F, 0x46)
    OP_24(0x110, 0x46)
    Sleep(100)
    OP_24(0x10F, 0x3C)
    OP_24(0x110, 0x3C)
    Sleep(100)
    OP_24(0x10F, 0x32)
    OP_24(0x110, 0x32)
    Sleep(100)
    OP_24(0x10F, 0x28)
    OP_24(0x110, 0x28)
    Sleep(100)
    OP_24(0x10F, 0x1E)
    OP_24(0x110, 0x1E)
    Sleep(100)
    OP_24(0x10F, 0x14)
    OP_24(0x110, 0x14)
    Sleep(100)
    OP_24(0x10F, 0xA)
    OP_24(0x110, 0xA)
    Sleep(100)
    OP_23(0x10F)
    OP_23(0x110)
    WaitChrThread(0x11, 0x2)
    Fade(1000)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_6D(23950, 0, 55930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x11, 0x0)
    OP_8C(0x109, 225, 0)
    OP_0D()
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)

    ChrTalk(    #43
        0x101,
        "#1020F#6PNo!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2621")

    ChrTalk(    #44
        0x106,
        "#054F#5PC'mon, after it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2639")

    label("loc_2621")


    ChrTalk(    #45
        0x103,
        "#024F#5PFollow it!\x02",
    )

    CloseMessageWindow()

    label("loc_2639")


    def lambda_263F():
        OP_8E(0xFE, 0x448E, 0x0, 0xC9EA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_263F)
    Sleep(100)

    def lambda_265F():
        OP_8E(0xFE, 0x3C1E, 0x0, 0xC3E6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_265F)
    Sleep(100)

    def lambda_267F():
        OP_8E(0xFE, 0x3F84, 0x0, 0xC45E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_267F)
    Sleep(1000)
    WaitChrThread(0xF7, 0x1)

    def lambda_26A4():
        OP_8E(0xFE, 0x3C5A, 0x0, 0xBFFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_26A4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    OP_DB()

    def lambda_26DA():

        label("loc_26DA")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_26DA")

    QueueWorkItem2(0x11, 0, lambda_26DA)
    SetChrPos(0x11, 13560, 0, 45760, 180)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(13560, 0, 45760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)

    def lambda_27AD():

        label("loc_27AD")

        OP_69(0x11, 0x0)
        OP_48()
        Jump("loc_27AD")

    QueueWorkItem2(0x11, 2, lambda_27AD)
    OP_22(0x10F, 0x0, 0x64)
    OP_22(0x110, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_8E(0x11, 0x34F8, 0x0, 0x8520, 0x1194, 0x0)
    OP_43(0x11, 0x1, 0x0, 0x12)

    def lambda_27EC():
        OP_8C(0xFE, 270, 52)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_27EC)
    OP_22(0x1FE, 0x0, 0x64)
    Sleep(200)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x1E)
    Sleep(10)
    OP_6F(0x5, 1)
    OP_70(0x5, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x1E)
    WaitChrThread(0x11, 0x1)
    OP_43(0x11, 0x1, 0x0, 0x13)
    OP_8C(0x11, 180, 60)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_24(0x75, 0x5A)
    Sleep(100)
    OP_24(0x75, 0x50)
    Sleep(100)
    OP_24(0x75, 0x46)
    Sleep(100)
    OP_24(0x75, 0x3C)
    Sleep(100)
    OP_24(0x75, 0x32)
    Sleep(100)
    OP_24(0x75, 0x28)
    Sleep(100)
    OP_24(0x75, 0x1E)
    Sleep(100)
    OP_24(0x75, 0x14)
    Sleep(100)
    OP_24(0x75, 0xA)
    Sleep(100)
    OP_23(0x75)
    WaitChrThread(0x11, 0x1)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/T4403   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1267 end

    def Function_13_28D7(): pass

    label("Function_13_28D7")

    Sleep(100)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x9100, 0x0, 0xE7F4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_13_28D7 end

    def Function_14_2919(): pass

    label("Function_14_2919")

    Sleep(150)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x915A, 0x0, 0xC468, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9182, 0x0, 0xC4AE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_14_2919 end

    def Function_15_296F(): pass

    label("Function_15_296F")

    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x9448, 0x0, 0xEA88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x96BE, 0x0, 0xEA56, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_15_296F end

    def Function_16_29C0(): pass

    label("Function_16_29C0")

    Sleep(50)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x93A8, 0x0, 0xC440, 0x7D0, 0x0)
    OP_8E(0xFE, 0x96DC, 0x0, 0xC4C2, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_16_29C0 end

    def Function_17_2A16(): pass

    label("Function_17_2A16")

    OP_8F(0xFE, 0x3CC8, 0x0, 0xBEBE, 0x1194, 0x0)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)
    OP_8F(0xFE, 0x38E0, 0x0, 0x88B8, 0x1194, 0x0)
    Return()

    # Function_17_2A16 end

    def Function_18_2A4D(): pass

    label("Function_18_2A4D")

    OP_8F(0xFE, 0x2184, 0x0, 0x690A, 0x1194, 0x0)
    OP_8F(0xFE, 0x94C, 0x0, 0x6522, 0x1194, 0x0)
    Return()

    # Function_18_2A4D end

    def Function_19_2A76(): pass

    label("Function_19_2A76")

    OP_8F(0xFE, 0xFFFFFC36, 0x0, 0x4C68, 0x1194, 0x0)
    OP_8F(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFDDBE, 0x1194, 0x0)
    Return()

    # Function_19_2A76 end

    def Function_20_2A9F(): pass

    label("Function_20_2A9F")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B18"),
        (1, "loc_2B1E"),
        (SWITCH_DEFAULT, "loc_2B24"),
    )


    label("loc_2B18")

    OP_A2(0x1200)
    Jump("loc_2B24")

    label("loc_2B1E")

    OP_A2(0x1201)
    Jump("loc_2B24")

    label("loc_2B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2B32")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_2B36")

    label("loc_2B32")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_2B36")

    Return()

    # Function_20_2A9F end

    SaveToFile()

Try(main)
