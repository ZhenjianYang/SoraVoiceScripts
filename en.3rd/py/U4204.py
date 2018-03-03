from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4204   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'Gilbert',                              # 9
        'Dummy Gilbert',                        # 10
        'Skull Head',                           # 11
        'Skull Head',                           # 12
        'Skull Head',                           # 13
        'Skull Head',                           # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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


    AddCharChip(
        'ED6_DT27/CH03750 ._CH',             # 00
        'ED6_DT26/CH20632 ._CH',             # 01
        'ED6_DT26/CH20451 ._CH',             # 02
        'ED6_DT29/CH14730 ._CH',             # 03
        'ED6_DT29/CH14730 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03750P._CP',             # 00
        'ED6_DT26/CH20632P._CP',             # 01
        'ED6_DT26/CH20451P._CP',             # 02
        'ED6_DT29/CH14730P._CP',             # 03
        'ED6_DT29/CH14730P._CP',             # 04
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -38510,
        Z                   = 16000,
        Y                   = 80480,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18850,
        Z                   = 14000,
        Y                   = 63840,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8189,
        Z                   = 18000,
        Y                   = 93900,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6280,
        Z                   = 12000,
        Y                   = 55830,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9340,
        Z                   = 12000,
        Y                   = 60550,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -530,
        Y                   = 13500,
        Z                   = 74660,
        Range               = 4019,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x14BA4,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 42000,
        TriggerZ            = 16000,
        TriggerY            = 80000,
        TriggerRange        = 1000,
        ActorX              = 42000,
        ActorZ              = 19000,
        ActorY              = 80000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41050,
        TriggerZ            = 16000,
        TriggerY            = 83370,
        TriggerRange        = 1000,
        ActorX              = -41050,
        ActorZ              = 17000,
        ActorY              = 83370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 12000,
        TriggerY            = 49000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 13000,
        ActorY              = 49000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2D6",          # 01, 1
        "Function_2_322",          # 02, 2
        "Function_3_46F",          # 03, 3
        "Function_4_5D0",          # 04, 4
        "Function_5_9F6",          # 05, 5
        "Function_6_A07",          # 06, 6
        "Function_7_14DB",         # 07, 7
        "Function_8_150B",         # 08, 8
        "Function_9_152C",         # 09, 9
        "Function_10_154D",        # 0A, 10
        "Function_11_1582",        # 0B, 11
        "Function_12_15C8",        # 0C, 12
        "Function_13_1605",        # 0D, 13
        "Function_14_2AF4",        # 0E, 14
        "Function_15_2B56",        # 0F, 15
        "Function_16_2BAF",        # 10, 16
        "Function_17_2D7F",        # 11, 17
        "Function_18_2E35",        # 12, 18
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2C0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_2D5")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2D5")

    Return()

    # Function_0_2AA end

    def Function_1_2D6(): pass

    label("Function_1_2D6")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2EC")
    OP_82(0x82, 0x0)
    Jump("loc_2EF")

    label("loc_2EC")

    OP_82(0x83, 0x0)

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301")
    OP_6F(0x2, 0)
    Jump("loc_308")

    label("loc_301")

    OP_6F(0x2, 60)

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A")
    OP_6F(0x3, 0)
    Jump("loc_321")

    label("loc_31A")

    OP_6F(0x3, 60)

    label("loc_321")

    Return()

    # Function_1_2D6 end

    def Function_2_322(): pass

    label("Function_2_322")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_390")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2798)
    Jump("loc_3F8")

    label("loc_390")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_3F8")

    Jump("loc_461")

    label("loc_3FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05What are you still doing here?! You're a priest, for Aidios' sake!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x125, 0x0)

    label("loc_461")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_322 end

    def Function_3_46F(): pass

    label("Function_3_46F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25F, 1)"), scpexpr(EXPR_END)), "loc_4DD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x5F\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2799)
    Jump("loc_545")

    label("loc_4DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x5F\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x5F\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_545")

    Jump("loc_5C2")

    label("loc_548")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Hey, Father! I have some new Stregas inside. Would you kindly come in\x01",
            "and try them on?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x126, 0x0)

    label("loc_5C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_46F end

    def Function_4_5D0(): pass

    label("Function_4_5D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 29170, 10000, 77810, 0)
    SetChrPos(0x10F, 30820, 10000, 77720, 0)
    SetChrPos(0xF0, 29170, 10000, 77810, 0)
    SetChrPos(0xF1, 30820, 10000, 77720, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 16430, 14000, 79490, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(31320, 14500, 84900, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)

    def lambda_684():
        OP_6D(31320, 12000, 84900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_684)

    def lambda_69C():
        OP_67(0, 5200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_69C)

    def lambda_6B4():
        OP_6B(3190, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6B4)

    def lambda_6C4():
        OP_6E(277, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6C4)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_6DE():
        OP_8E(0xFE, 0x724C, 0x2EE0, 0x149E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6DE)
    Sleep(200)

    def lambda_6FE():
        OP_8E(0xFE, 0x783C, 0x2EE0, 0x148E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6FE)
    Sleep(550)

    def lambda_71E():
        OP_8E(0xFE, 0x7256, 0x2EE0, 0x14492, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_71E)
    Sleep(230)

    def lambda_73E():
        OP_8E(0xFE, 0x7864, 0x2EE0, 0x14384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_73E)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #6
        0x10,
        "Young Man's Voice",
        (
            "#2PEeek!\x02\x03",

            "Stay away! Stay away!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_803")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_86A")

    label("loc_803")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_86A")

    label("loc_82B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_86A")

    label("loc_853")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_86A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8FE")

    label("loc_897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8FE")

    label("loc_8BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8FE")

    label("loc_8E7")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8FE")

    Sleep(1000)

    def lambda_909():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_909)
    Sleep(100)

    def lambda_91C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_91C)
    Sleep(100)

    def lambda_92F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_92F)
    Sleep(100)
    OP_8C(0xF1, 270, 400)

    ChrTalk(    #7
        0x10E,
        "#173F#5PThat was a human's voice, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        "#1069F#5PSo there's someone still safe here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1443F#5PWe should hurry and find them right away.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2717)
    OP_28(0x2D, 0x1, 0x10)
    SetChrFlags(0x10, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_5D0 end

    def Function_5_9F6(): pass

    label("Function_5_9F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 0)), scpexpr(EXPR_END)), "loc_9FE")
    Return()

    label("loc_9FE")

    Call(0, 6)
    Call(0, 13)
    Return()

    # Function_5_9F6 end

    def Function_6_A07(): pass

    label("Function_6_A07")

    EventBegin(0x0)
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -27320, 12000, 88230, 135)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x12, -27230, 12300, 81740, 0)
    SetChrPos(0x13, -24960, 12300, 83030, 315)
    SetChrPos(0x14, -23210, 12300, 84810, 315)
    SetChrPos(0x15, -21660, 12300, 87480, 270)

    def lambda_AB0():

        label("loc_AB0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AB0")

    QueueWorkItem2(0x12, 3, lambda_AB0)

    def lambda_AC3():

        label("loc_AC3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AC3")

    QueueWorkItem2(0x13, 3, lambda_AC3)

    def lambda_AD6():

        label("loc_AD6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AD6")

    QueueWorkItem2(0x14, 3, lambda_AD6)

    def lambda_AE9():

        label("loc_AE9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AE9")

    QueueWorkItem2(0x15, 3, lambda_AE9)
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_B21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B47")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_B47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6D")
    OP_62(0x0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_B6D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B93")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_B93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_BB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDF")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C02")

    label("loc_BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C02")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C02")

    Sleep(1000)

    def lambda_C0D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C0D)

    def lambda_C1B():
        OP_6D(-26940, 12000, 89180, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C1B)

    def lambda_C33():
        OP_67(0, 6170, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C33)

    def lambda_C4B():
        OP_6B(3440, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C4B)

    def lambda_C5B():
        OP_6C(357000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C5B)

    def lambda_C6B():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C6B)
    Sleep(2500)
    OP_1D(0xB4)

    def lambda_C82():
        OP_8F(0xFE, 0xFFFF9FD4, 0x300C, 0x15126, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C82)
    Sleep(50)

    def lambda_CA2():
        OP_8F(0xFE, 0xFFFF9462, 0x300C, 0x14712, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CA2)
    Sleep(100)

    def lambda_CC2():
        OP_8F(0xFE, 0xFFFFA2F4, 0x300C, 0x15964, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_CC2)
    Sleep(50)

    def lambda_CE2():
        OP_8F(0xFE, 0xFFFF9AC0, 0x300C, 0x14B86, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CE2)
    Sleep(100)

    def lambda_D02():
        OP_8F(0xFE, 0xFFFF90F2, 0x2EE0, 0x15DBA, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D02)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 180, 400)
    Sleep(500)
    OP_8C(0x10, 90, 400)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #10
        0x10,
        "#1224F#5PWh-What did I do to deserve this?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    Fade(500)

    def lambda_DA6():
        OP_6D(-27730, 12000, 89650, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DA6)

    def lambda_DBE():
        OP_67(0, 6170, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DBE)

    def lambda_DD6():
        OP_6B(3300, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DD6)

    def lambda_DE6():
        OP_6E(265, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DE6)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(300)

    ChrTalk(    #11
        0x10,
        "#1227F#5PSt-Stay back! Don't come any closer! Please!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    WaitChrThread(0x10, 0x0)
    OP_43(0x10, 0x0, 0x0, 0xC)
    SetChrPos(0x109, 2500, 14000, 78640, 270)
    SetChrPos(0x10F, 2500, 14000, 80240, 270)
    SetChrPos(0xF0, 4100, 14000, 81150, 270)
    SetChrPos(0xF1, 3810, 14000, 78010, 270)
    Fade(500)
    OP_6D(4750, 14000, 80700, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(271, 0)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -27610, 12000, 88750, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F63")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FCA")

    label("loc_F63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8B")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FCA")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB3")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FCA")

    label("loc_FB3")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_FCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF2")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101A")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_101A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1042")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_1042")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1059")

    Sleep(2000)

    ChrTalk(    #12
        0x10E,
        "#178F#5P...What is this curious spectacle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        "#1068F#5PCrap... I'd forgotten all about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F#5PSo had I...\x02\x03",

            "#1802FI suppose it's no surprise he ended up here,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F#5PSucks to admit, but you're right.\x02\x03",

            "#1063FAnd it sucks even more 'cause I've got a whole\x01",
            "lot of questions I want to ask him, and the only\x01",
            "way I'm getting 'em is to bail him out!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 6)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 9)
    SetChrSubChip(0xF0, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x7)
    OP_43(0x10F, 0x0, 0x0, 0x8)
    OP_43(0xF0, 0x0, 0x0, 0x9)
    OP_43(0xF1, 0x0, 0x0, 0xA)

    def lambda_124F():
        OP_6D(-22980, 12000, 86370, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_124F)

    def lambda_1267():
        OP_67(0, 5870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1267)

    def lambda_127F():
        OP_6B(4530, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_127F)

    def lambda_128F():
        OP_6C(355000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_128F)

    def lambda_129F():
        OP_6E(238, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_129F)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #16
        0x109,
        "#1069F#6PGet away from him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        (
            "#1443FIf you're unable to leave behind your attachment\x01",
            "to this world, allow us to help you.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0x0)
    OP_62(0x11, 0xFFFFFF38, 1100, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrFlags(0x11, 0x80)
    SetChrSubChip(0x10, 0)
    OP_0D()

    def lambda_1388():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1388)
    Sleep(100)

    def lambda_139B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_139B)
    Sleep(100)

    def lambda_13AE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_13AE)
    Sleep(100)

    def lambda_13C1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_13C1)

    ChrTalk(    #18
        0x10,
        (
            "#1224F#5PWh-What are you gu--?\x01",
            "I mean, what are you wonderful, angelic,\x01",
            "model human beings doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1069F#6PSave the sweet talking for later! First,\x01",
            "we need to take these things out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10F,
        "#1446F#4PJust stay there, and don't get in our way.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0xF7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_A07 end

    def Function_7_14DB(): pass

    label("Function_7_14DB")

    OP_8E(0xFE, 0xFFFFDDC8, 0x36B0, 0x1327C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB410, 0x36B0, 0x132D6, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_14DB end

    def Function_8_150B(): pass

    label("Function_8_150B")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFB8A2, 0x36B0, 0x136BE, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_8_150B end

    def Function_9_152C(): pass

    label("Function_9_152C")

    Sleep(600)
    OP_8E(0xFE, 0xFFFFBD2A, 0x36B0, 0x1311E, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_9_152C end

    def Function_10_154D(): pass

    label("Function_10_154D")

    Sleep(400)
    OP_8E(0xFE, 0xFFFFDDC8, 0x36B0, 0x1327C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB82A, 0x36B0, 0x12D2C, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_10_154D end

    def Function_11_1582(): pass

    label("Function_11_1582")

    OP_22(0x218, 0x0, 0x64)
    OP_99(0x10, 0x0, 0x6, 0x5DC)
    Sleep(1000)

    label("loc_1595")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C7")
    OP_99(0x10, 0x6, 0x2, 0x5DC)
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x10, 0x2, 0x6, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15C4")
    Jump("loc_15C7")

    label("loc_15C4")

    Jump("loc_1595")

    label("loc_15C7")

    Return()

    # Function_11_1582 end

    def Function_12_15C8(): pass

    label("Function_12_15C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1604")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_12_15C8")

    label("loc_1604")

    Return()

    # Function_12_15C8 end

    def Function_13_1605(): pass

    label("Function_13_1605")

    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    SetChrPos(0x109, -26770, 12000, 89610, 135)
    SetChrPos(0x10F, -27850, 12000, 88130, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1692")
    SetChrPos(0x10E, -29230, 12000, 88830, 135)
    SetChrPos(0xF1, -27480, 12000, 91150, 135)
    Jump("loc_16C2")

    label("loc_1692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C2")
    SetChrPos(0x10E, -29230, 12000, 88830, 135)
    SetChrPos(0xF0, -27480, 12000, 91150, 135)

    label("loc_16C2")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -29200, 12000, 91300, 135)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 1)
    ClearChrFlags(0x10, 0x800)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -28770, 12000, 91170, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_6D(-24780, 12000, 88360, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(8000, 0)
    OP_6E(224, 0)

    def lambda_178C():
        OP_6D(-27700, 12000, 91910, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_178C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #21
        0x10,
        (
            "#1220F#5PI-I'm alive...\x02\x03",

            "#1221FThank you so much! You saved--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17FB():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_17FB)
    WaitChrThread(0x10F, 0x0)

    def lambda_180E():
        OP_8F(0xFE, 0xFFFF9322, 0x2EE0, 0x15DD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_180E)

    def lambda_1829():
        OP_6D(-28370, 12000, 92120, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1829)

    def lambda_1841():
        OP_67(0, 6170, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1841)

    def lambda_1859():
        OP_6B(4140, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1859)

    def lambda_1869():
        OP_6C(357000, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1869)

    def lambda_1879():
        OP_6E(224, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1879)

    def lambda_1889():

        label("loc_1889")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_1889")

    QueueWorkItem2(0x109, 3, lambda_1889)
    Sleep(100)

    def lambda_189F():

        label("loc_189F")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_189F")

    QueueWorkItem2(0xF0, 3, lambda_189F)
    Sleep(100)

    def lambda_18B5():

        label("loc_18B5")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_18B5")

    QueueWorkItem2(0xF1, 3, lambda_18B5)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x10F, 0x3)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)

    def lambda_18E4():
        OP_6B(3740, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_18E4)

    def lambda_18F4():
        OP_6E(225, 500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_18F4)
    OP_0D()
    OP_62(0x11, 0x0, 1400, 0x28, 0x2B, 0x50, 0x0)
    Sleep(1000)
    OP_63(0x11)
    OP_44(0x109, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)

    ChrTalk(    #22
        0x10,
        "#1224F#5PEeeeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        (
            "#1446F#6PNow it's time for you to answer some questions\x01",
            "for us.\x02\x03",

            "#1440FIs there anything you'd like to ask him, Captain?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F9")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1A60")

    label("loc_19F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A21")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1A60")

    label("loc_1A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A49")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1A60")

    label("loc_1A49")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1A60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A88")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AEF")

    label("loc_1A88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB0")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AEF")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD8")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AEF")

    label("loc_1AD8")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1AEF")

    Sleep(1000)

    ChrTalk(    #24
        0x10E,
        "#173F#6PA-As it so happens, yes.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B58")

    def lambda_1B2E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1B2E)
    Sleep(100)

    def lambda_1B41():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B41)
    Sleep(100)
    OP_8C(0xF1, 270, 400)
    Jump("loc_1B93")

    label("loc_1B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B93")

    def lambda_1B6C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1B6C)
    Sleep(100)

    def lambda_1B7F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B7F)
    Sleep(100)
    OP_8C(0xF0, 270, 400)

    label("loc_1B93")

    Sleep(300)

    ChrTalk(    #25
        0x10E,
        (
            "#178F#6PHow exactly did you come to be here...Gilbert,\x01",
            "I believe?\x02\x03",

            "Do you know anything regarding how the capital\x01",
            "came to be this way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#1224F#5PN-N-No, I don't...\x02\x03",

            "I just woke up and found m-myself in the port\x01",
            "here. I don't know why or how.\x02\x03",

            "I went into town, but there was no one there.\x01",
            "Just a bunch of weird, armored knights...\x02\x03",

            "I started running away from them and next\x01",
            "thing I knew, I f-found myself in this castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1065FHmm... So you were sent to a different place\x01",
            "than us, huh?\x02\x03",

            "#1067FToo bad the city had already gone weird by\x01",
            "the time you woke up.\x02\x03",

            "#1840FI was kinda banking on you witnessing\x01",
            "whatever happened here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "#1222F#5PHmph. Well, boo hoo for you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F66")

    ChrTalk(    #29
        0x102,
        (
            "#1505F#2PI've got something I want to ask you, too.\x02\x03",

            "#1502FIs Ouroboros involved in this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#1222F#5PSo you're here, too, Joshua?\x02\x03",

            "#1226FB-Bah... Of course not!\x02\x03",

            "#1221FIf they were, I obviously would've been\x01",
            "the first to know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1508F#2P(More like the last.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2108")

    label("loc_1F66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2108")

    ChrTalk(    #32
        0x10B,
        (
            "#213F#2PHey, so while we're asking questions...\x02\x03",

            "#416F...I just remembered how that one Ouroboros\x01",
            "airship tried to knock us out of the sky a while\x01",
            "back.\x02\x03",

            "#210FYou weren't a part of all that personally, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1400, 0x28, 0x2B, 0x50, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #33
        0x10,
        (
            "#1224F#5PHow did you...?\x02\x03",

            "#1226FI-I mean, of course not! HA HA HA! Why would\x01",
            "you ever think that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10B,
        "#212F#2P(He couldn't be more suspicious if he tried...)\x02",
    )

    CloseMessageWindow()

    label("loc_2108")


    ChrTalk(    #35
        0x10F,
        (
            "#1443F#6PWhat should we do with him, Kevin?\x02\x03",

            "Disarm him and tie him up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1060FIt's fine. He's not worth the trouble.\x02\x03",

            "He doesn't seem to know anything worthwhile,\x01",
            "and he'd just get in our way, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1446F#6P...I suppose that's true.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #38
        0x10F,
        (
            "#1805F#6PWell, that's all the business we have with you.\x02\x03",

            "Kindly remove yourself from our sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1222F#5PThink you c-can make me out to be some kind\x01",
            "of useless fop, do you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_22FA():
        OP_96(0xFE, 0xFFFF8B8E, 0x2EE0, 0x16792, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_22FA)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x10,
        (
            "#1225F#5PW-Well, you'll regret this!\x02\x03",

            "When I find a way out of this place, you're gonna\x01",
            "be begging me to share it with you--but I WON'T!\x02\x03",

            "You can wander here lost for all eternity for all\x01",
            "I care!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23F1():
        OP_6D(-24990, 12000, 88510, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23F1)

    def lambda_2409():
        OP_67(0, 6170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2409)

    def lambda_2421():
        OP_6B(4140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2421)

    def lambda_2431():
        OP_6C(8000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2431)

    def lambda_2441():
        OP_6E(224, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2441)
    OP_43(0x10, 0x0, 0x0, 0xE)

    def lambda_2458():

        label("loc_2458")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2458")

    QueueWorkItem2(0x109, 3, lambda_2458)

    def lambda_2469():

        label("loc_2469")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2469")

    QueueWorkItem2(0x10F, 3, lambda_2469)

    def lambda_247A():

        label("loc_247A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_247A")

    QueueWorkItem2(0xF0, 3, lambda_247A)

    def lambda_248B():

        label("loc_248B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_248B")

    QueueWorkItem2(0xF1, 3, lambda_248B)
    WaitChrThread(0x109, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2506")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_256D")

    label("loc_2506")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252E")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_256D")

    label("loc_252E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2556")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_256D")

    label("loc_2556")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_256D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2595")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_25FC")

    label("loc_2595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BD")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_25FC")

    label("loc_25BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E5")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_25FC")

    label("loc_25E5")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_25FC")

    Sleep(1500)

    def lambda_2607():
        OP_6D(-27650, 12000, 91300, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2607)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2720")

    ChrTalk(    #41
        0x107,
        (
            "#561F#5PUmm...\x02\x03",

            "#063FAre you sure he's going to be all right on his\x01",
            "own? I don't know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1060F#5PCockroaches can live through anything, sweet\x01",
            "Tita.\x02\x03",

            "And he IS technically a member of Ouroboros.\x01",
            "I'm sure he can look after himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_2720")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2847")

    ChrTalk(    #43
        0x10D,
        (
            "#272F#5PWhat a nuisance...\x02\x03",

            "#270FI hope leaving him on his own doesn't go causing\x01",
            "more trouble for us in the long run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x109,
        (
            "#1060F#5PTell me, Mueller, was that the face of a guy\x01",
            "who's capable of wreaking major havoc?\x02\x03",

            "I'm sure he'll be fine enough to stay out of\x01",
            "our hair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_2847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2962")

    ChrTalk(    #45
        0x10B,
        (
            "#212F#5PAre you sure he's gonna be okay on his own?\x02\x03",

            "The fiends in these parts are pretty strong,\x01",
            "and he's about as tough as an old sponge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        (
            "#1060F#5PNah. I'm sure he'll be fine.\x02\x03",

            "He IS technically a member of Ouroboros.\x01",
            "I'm sure he can look after himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_2962")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A75")

    ChrTalk(    #47
        0x10E,
        (
            "#176F#5PI can't help but feel a little concerned.\x02\x03",

            "#178FI hope he doesn't end up causing any\x01",
            "trouble after being left on his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        (
            "#1060F#5PEh, I'm sure it'll be fine.\x02\x03",

            "He seems like the type who could worm his\x01",
            "way out of any situation you hand him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A75")


    ChrTalk(    #49
        0x10F,
        (
            "#1446F#5PI believe we've wasted enough of our time\x01",
            "on him.\x02\x03",

            "#1440FWe should resume exploring the castle.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2718)
    OP_28(0x2D, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_1605 end

    def Function_14_2AF4(): pass

    label("Function_14_2AF4")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF8896, 0x2EE0, 0x159E6, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFA43E, 0x2EE0, 0x143D4, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFBECE, 0x36B0, 0x1322C, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFF844, 0x36B0, 0x1340C, 0x2710, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_14_2AF4 end

    def Function_15_2B56(): pass

    label("Function_15_2B56")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_15_2B56 end

    def Function_16_2BAF(): pass

    label("Function_16_2BAF")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 39330, 16000, 80640, 90)
    SetChrPos(0x1, 39220, 16000, 78880, 90)
    SetChrPos(0x2, 37290, 16000, 80610, 90)
    SetChrPos(0x3, 36890, 16000, 78640, 90)
    OP_6D(38230, 16000, 79470, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C85")
    OP_28(0x7, 0x4, 0x2)
    OP_82(0x82, 0x2)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2C85")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05#40WBring to me the boy with eyes of amber\x01",
            "and the princess with an indomitable will.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D73")
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D70")
    Call(0, 17)

    label("loc_2D70")

    Jump("loc_2D73")

    label("loc_2D73")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_16_2BAF end

    def Function_17_2D7F(): pass

    label("Function_17_2D7F")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)

    def lambda_2DE8():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2DE8)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x5, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2D7F end

    def Function_18_2E35(): pass

    label("Function_18_2E35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 39330, 16000, 80640, 90)
    SetChrPos(0x1, 39220, 16000, 78880, 90)
    SetChrPos(0x2, 37290, 16000, 80610, 90)
    SetChrPos(0x3, 36890, 16000, 78640, 90)
    OP_6D(38230, 16000, 79470, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_18_2E35 end

    SaveToFile()

Try(main)
