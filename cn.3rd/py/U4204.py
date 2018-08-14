from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '基尔巴特',                             # 9
        '临时基尔巴特',                         # 10
        '骷髅邪首',                             # 11
        '骷髅邪首',                             # 12
        '骷髅邪首',                             # 13
        '骷髅邪首',                             # 14
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
        "Function_3_448",          # 03, 3
        "Function_4_56E",          # 04, 4
        "Function_5_985",          # 05, 5
        "Function_6_996",          # 06, 6
        "Function_7_1380",         # 07, 7
        "Function_8_13B0",         # 08, 8
        "Function_9_13D1",         # 09, 9
        "Function_10_13F2",        # 0A, 10
        "Function_11_1427",        # 0B, 11
        "Function_12_146D",        # 0C, 12
        "Function_13_14AA",        # 0D, 13
        "Function_14_268A",        # 0E, 14
        "Function_15_26EC",        # 0F, 15
        "Function_16_2760",        # 10, 16
        "Function_17_292A",        # 11, 17
        "Function_18_29E0",        # 12, 18
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_396")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_37B")

    label("loc_37B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2798)
    Jump("loc_404")

    label("loc_396")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3E5")

    label("loc_3E5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_404")

    Jump("loc_43A")

    label("loc_407")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_43A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_322 end

    def Function_3_448(): pass

    label("Function_3_448")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25F, 1)"), scpexpr(EXPR_END)), "loc_4BC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x5F\x02\x07\x00。\x02",
    )

    Jump("loc_4A1")

    label("loc_4A1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2799)
    Jump("loc_52A")

    label("loc_4BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x5F\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x5F\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_50B")

    label("loc_50B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_52A")

    Jump("loc_560")

    label("loc_52D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_560")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_448 end

    def Function_4_56E(): pass

    label("Function_4_56E")

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

    def lambda_622():
        OP_6D(31320, 12000, 84900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_622)

    def lambda_63A():
        OP_67(0, 5200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_63A)

    def lambda_652():
        OP_6B(3190, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_652)

    def lambda_662():
        OP_6E(277, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_662)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_67C():
        OP_8E(0xFE, 0x724C, 0x2EE0, 0x149E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67C)
    Sleep(200)

    def lambda_69C():
        OP_8E(0xFE, 0x783C, 0x2EE0, 0x148E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_69C)
    Sleep(550)

    def lambda_6BC():
        OP_8E(0xFE, 0x7256, 0x2EE0, 0x14492, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6BC)
    Sleep(230)

    def lambda_6DC():
        OP_8E(0xFE, 0x7864, 0x2EE0, 0x14384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6DC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #6
        0x10,
        "青年的声音",
        (
            "#2P哇、哇啊……\x02\x03",

            "别过来……\x01",
            "……别过来啊…… \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_81D")

    label("loc_7B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_81D")

    label("loc_7DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_81D")

    label("loc_806")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_81D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8B1")

    label("loc_84A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8B1")

    label("loc_872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8B1")

    label("loc_89A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8B1")

    Sleep(1000)

    def lambda_8BC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8BC)
    Sleep(100)

    def lambda_8CF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8CF)
    Sleep(100)

    def lambda_8E2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8E2)
    Sleep(100)
    OP_8C(0xF1, 270, 400)

    ChrTalk(    #7
        0x10E,
        "#173F#5P是人的声音……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        "#1069F#5P有幸存的人吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1443F#5P…………快过去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2717)
    OP_28(0x2D, 0x1, 0x10)
    SetChrFlags(0x10, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_56E end

    def Function_5_985(): pass

    label("Function_5_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 0)), scpexpr(EXPR_END)), "loc_98D")
    Return()

    label("loc_98D")

    Call(0, 6)
    Call(0, 13)
    Return()

    # Function_5_985 end

    def Function_6_996(): pass

    label("Function_6_996")

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

    def lambda_A3F():

        label("loc_A3F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A3F")

    QueueWorkItem2(0x12, 3, lambda_A3F)

    def lambda_A52():

        label("loc_A52")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A52")

    QueueWorkItem2(0x13, 3, lambda_A52)

    def lambda_A65():

        label("loc_A65")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A65")

    QueueWorkItem2(0x14, 3, lambda_A65)

    def lambda_A78():

        label("loc_A78")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A78")

    QueueWorkItem2(0x15, 3, lambda_A78)
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_AB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD6")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_AD6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC")
    OP_62(0x0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_AFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B22")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_B22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_B48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6E")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B91")

    label("loc_B6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B91")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B91")

    Sleep(1000)

    def lambda_B9C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B9C)

    def lambda_BAA():
        OP_6D(-26940, 12000, 89180, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BAA)

    def lambda_BC2():
        OP_67(0, 6170, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BC2)

    def lambda_BDA():
        OP_6B(3440, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BDA)

    def lambda_BEA():
        OP_6C(357000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BEA)

    def lambda_BFA():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_BFA)
    Sleep(2500)
    OP_1D(0xB4)

    def lambda_C11():
        OP_8F(0xFE, 0xFFFF9FD4, 0x300C, 0x15126, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C11)
    Sleep(50)

    def lambda_C31():
        OP_8F(0xFE, 0xFFFF9462, 0x300C, 0x14712, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C31)
    Sleep(100)

    def lambda_C51():
        OP_8F(0xFE, 0xFFFFA2F4, 0x300C, 0x15964, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C51)
    Sleep(50)

    def lambda_C71():
        OP_8F(0xFE, 0xFFFF9AC0, 0x300C, 0x14B86, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C71)
    Sleep(100)

    def lambda_C91():
        OP_8F(0xFE, 0xFFFF90F2, 0x2EE0, 0x15DBA, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C91)
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
        "#1224F#5P为、为什么会遇上这种事……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    Fade(500)

    def lambda_D35():
        OP_6D(-27730, 12000, 89650, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D35)

    def lambda_D4D():
        OP_67(0, 6170, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D4D)

    def lambda_D65():
        OP_6B(3300, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D65)

    def lambda_D75():
        OP_6E(265, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_D75)
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
        (
            "#1227F#5P别、别过来……\x01",
            "求你们别过来啊！\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_F53")

    label("loc_EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_F53")

    label("loc_F14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3C")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_F53")

    label("loc_F3C")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_F53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7B")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FE2")

    label("loc_F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA3")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FE2")

    label("loc_FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCB")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_FE2")

    label("loc_FCB")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_FE2")

    Sleep(2000)

    ChrTalk(    #12
        0x10E,
        "#178F#5P……那是什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1068F#5P对了……\x01",
            "我已经全给忘了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F#5P……嗯，我也是。\x02\x03",

            "#1802F不过就算他被卷进来\x01",
            "也不值得奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F#5P是啊……\x02\x03",

            "#1063F……算了。\x01",
            "反正也有事情想打听一下，\x01",
            "总之先去救救他吧！\x02",
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

    def lambda_116E():
        OP_6D(-22980, 12000, 86370, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116E)

    def lambda_1186():
        OP_67(0, 5870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1186)

    def lambda_119E():
        OP_6B(4530, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_119E)

    def lambda_11AE():
        OP_6C(355000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_11AE)

    def lambda_11BE():
        OP_6E(238, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_11BE)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #16
        0x109,
        "#1069F#6P到此为止了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        (
            "#1443F……如果还有什么眷恋的话，\x01",
            "就让我们来当对手吧。\x02",
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

    def lambda_128D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_128D)
    Sleep(100)

    def lambda_12A0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_12A0)
    Sleep(100)

    def lambda_12B3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_12B3)
    Sleep(100)

    def lambda_12C6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_12C6)

    ChrTalk(    #18
        0x10,
        (
            "#1224F#5P你、你们这些──\x01",
            "不，是你们几位！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1069F#6P一会儿再说！\x01",
            "先把这些家伙干掉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10F,
        (
            "#1446F#4P……可不要\x01",
            "拖我们的后腿哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0xF7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_996 end

    def Function_7_1380(): pass

    label("Function_7_1380")

    OP_8E(0xFE, 0xFFFFDDC8, 0x36B0, 0x1327C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB410, 0x36B0, 0x132D6, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_1380 end

    def Function_8_13B0(): pass

    label("Function_8_13B0")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFB8A2, 0x36B0, 0x136BE, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_8_13B0 end

    def Function_9_13D1(): pass

    label("Function_9_13D1")

    Sleep(600)
    OP_8E(0xFE, 0xFFFFBD2A, 0x36B0, 0x1311E, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_9_13D1 end

    def Function_10_13F2(): pass

    label("Function_10_13F2")

    Sleep(400)
    OP_8E(0xFE, 0xFFFFDDC8, 0x36B0, 0x1327C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB82A, 0x36B0, 0x12D2C, 0x1770, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_10_13F2 end

    def Function_11_1427(): pass

    label("Function_11_1427")

    OP_22(0x218, 0x0, 0x64)
    OP_99(0x10, 0x0, 0x6, 0x5DC)
    Sleep(1000)

    label("loc_143A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_146C")
    OP_99(0x10, 0x6, 0x2, 0x5DC)
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x10, 0x2, 0x6, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1469")
    Jump("loc_146C")

    label("loc_1469")

    Jump("loc_143A")

    label("loc_146C")

    Return()

    # Function_11_1427 end

    def Function_12_146D(): pass

    label("Function_12_146D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14A9")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_12_146D")

    label("loc_14A9")

    Return()

    # Function_12_146D end

    def Function_13_14AA(): pass

    label("Function_13_14AA")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1537")
    SetChrPos(0x10E, -29230, 12000, 88830, 135)
    SetChrPos(0xF1, -27480, 12000, 91150, 135)
    Jump("loc_1567")

    label("loc_1537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1567")
    SetChrPos(0x10E, -29230, 12000, 88830, 135)
    SetChrPos(0xF0, -27480, 12000, 91150, 135)

    label("loc_1567")

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

    def lambda_1631():
        OP_6D(-27700, 12000, 91910, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1631)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #21
        0x10,
        (
            "#1220F#5P得、得救了……\x02\x03",

            "#1221F谢谢！\x01",
            "你们真是救命的恩人——\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16AD():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_16AD)
    WaitChrThread(0x10F, 0x0)

    def lambda_16C0():
        OP_8F(0xFE, 0xFFFF9322, 0x2EE0, 0x15DD8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_16C0)

    def lambda_16DB():
        OP_6D(-28370, 12000, 92120, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16DB)

    def lambda_16F3():
        OP_67(0, 6170, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16F3)

    def lambda_170B():
        OP_6B(4140, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_170B)

    def lambda_171B():
        OP_6C(357000, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_171B)

    def lambda_172B():
        OP_6E(224, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_172B)

    def lambda_173B():

        label("loc_173B")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_173B")

    QueueWorkItem2(0x109, 3, lambda_173B)
    Sleep(100)

    def lambda_1751():

        label("loc_1751")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_1751")

    QueueWorkItem2(0xF0, 3, lambda_1751)
    Sleep(100)

    def lambda_1767():

        label("loc_1767")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_1767")

    QueueWorkItem2(0xF1, 3, lambda_1767)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x10F, 0x3)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)

    def lambda_1796():
        OP_6B(3740, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1796)

    def lambda_17A6():
        OP_6E(225, 500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_17A6)
    OP_0D()
    OP_62(0x11, 0x0, 1400, 0x28, 0x2B, 0x50, 0x0)
    Sleep(1000)
    OP_63(0x11)
    OP_44(0x109, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)

    ChrTalk(    #22
        0x10,
        "#1224F#5P哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        (
            "#1446F#6P那么，接下来是质问时间。\x02\x03",

            "#1440F……尤莉亚上尉。\x01",
            "有什么想问的就请吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1894")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_18FB")

    label("loc_1894")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BC")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_18FB")

    label("loc_18BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E4")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_18FB")

    label("loc_18E4")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_18FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1923")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_198A")

    label("loc_1923")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194B")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_198A")

    label("loc_194B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1973")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_198A")

    label("loc_1973")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_198A")

    Sleep(1000)

    ChrTalk(    #24
        0x10E,
        "#173F#6P啊，好的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EE")

    def lambda_19C4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_19C4)
    Sleep(100)

    def lambda_19D7():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19D7)
    Sleep(100)
    OP_8C(0xF1, 270, 400)
    Jump("loc_1A29")

    label("loc_19EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A29")

    def lambda_1A02():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1A02)
    Sleep(100)

    def lambda_1A15():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A15)
    Sleep(100)
    OP_8C(0xF0, 270, 400)

    label("loc_1A29")

    Sleep(300)

    ChrTalk(    #25
        0x10E,
        (
            "#178F#6P你是叫基尔巴特吧……\x01",
            "为什么你会在这里？\x02\x03",

            "关于王都的异变，\x01",
            "你知道些什么吗？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#1224F#5P什、什、什么……\x02\x03",

            "当、当我醒过来的时候\x01",
            "已经躺在码头了……\x02\x03",

            "街、街上找不到任何人，\x01",
            "尽是些甲胄怪物之类的东西\x01",
            "在到处徘徊……\x02\x03",

            "然后我到处逃跑，\x01",
            "就、就到这城里来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1065F原来如此，\x01",
            "和我们不一样，\x01",
            "没有被传送到据点去啊。\x02\x03",

            "#1067F可是，醒过来之后\x01",
            "街上已经变成这幅样子了吗……\x02\x03",

            "#1840F如果能目击到\x01",
            "异界化时的情景就好了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "#1222F#5P哼……说的容易。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8C")

    ChrTalk(    #29
        0x102,
        (
            "#1505F#2P……基尔巴特。\x01",
            "我想问你一件事。\x02\x03",

            "#1502F这件事情和\x01",
            "『噬身之蛇』有关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#1222F#5P约修亚·布莱特……\x01",
            "……你也在啊……\x02\x03",

            "#1226F哼，\x01",
            "肯定和『结社』没有关系吧。\x02\x03",

            "#1221F不管怎么说，\x01",
            "我对此事一无所知\x01",
            "就是最好的证据！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1508F#2P（这根本算不上\x01",
            "  什么证据啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAD")

    ChrTalk(    #32
        0x10B,
        (
            "#213F#2P说起来……\x02\x03",

            "#416F之前，\x01",
            "你们的飞艇竟敢对\x01",
            "我们的山猫号出手……\x02\x03",

            "#210F……是不是\x01",
            "你干的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1400, 0x28, 0x2B, 0x50, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #33
        0x10,
        (
            "#1224F#5P呜……\x02\x03",

            "#1226F哈～哈～那～样的事～情\x01",
            "怎么～可能～是～我呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10B,
        "#212F#2P（真可疑……）\x02",
    )

    CloseMessageWindow()

    label("loc_1EAD")


    ChrTalk(    #35
        0x10F,
        (
            "#1443F#6P……凯文。\x01",
            "我们拿他怎么办？\x02\x03",

            "要把他解除武装看守起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1060F不……\x01",
            "这么做没必要吧。\x02\x03",

            "反正他也什么都不知道，\x01",
            "只会给我们添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1446F#6P……明白了。\x02",
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
            "#1805F#6P我们的话已经问完了。\x02\x03",

            "你可以消失\x01",
            "到一边去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1222F#5P你、你这家伙……\x01",
            "到底要侮辱我到什么程度……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_2043():
        OP_96(0xFE, 0xFFFF8B8E, 0x2EE0, 0x16792, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2043)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(300)

    ChrTalk(    #40
        0x10,
        (
            "#1225F#5P给、给我记住！\x02\x03",

            "就算我知道了\x01",
            "怎么从这个地方出去\x01",
            "也不会告诉你们的！\x02\x03",

            "你们就永远迷失在这个地方吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20F5():
        OP_6D(-24990, 12000, 88510, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20F5)

    def lambda_210D():
        OP_67(0, 6170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_210D)

    def lambda_2125():
        OP_6B(4140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2125)

    def lambda_2135():
        OP_6C(8000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2135)

    def lambda_2145():
        OP_6E(224, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2145)
    OP_43(0x10, 0x0, 0x0, 0xE)

    def lambda_215C():

        label("loc_215C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_215C")

    QueueWorkItem2(0x109, 3, lambda_215C)

    def lambda_216D():

        label("loc_216D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_216D")

    QueueWorkItem2(0x10F, 3, lambda_216D)

    def lambda_217E():

        label("loc_217E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_217E")

    QueueWorkItem2(0xF0, 3, lambda_217E)

    def lambda_218F():

        label("loc_218F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_218F")

    QueueWorkItem2(0xF1, 3, lambda_218F)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220A")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2271")

    label("loc_220A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2232")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2271")

    label("loc_2232")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225A")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2271")

    label("loc_225A")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2299")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2300")

    label("loc_2299")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C1")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2300")

    label("loc_22C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E9")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2300")

    label("loc_22E9")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2300")

    Sleep(1500)

    def lambda_230B():
        OP_6D(-27650, 12000, 91300, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_230B)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E5")

    ChrTalk(    #41
        0x107,
        (
            "#561F#5P哎，那个……\x02\x03",

            "#063F就这样把他一个人丢下\x01",
            "会不会有问题呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1060F#5P嗨，没关系的。\x02\x03",

            "怎么说也是『结社』的一员，\x01",
            "总该能照顾好自己吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2624")

    label("loc_23E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A1")

    ChrTalk(    #43
        0x10D,
        (
            "#272F#5P哎呀……\x02\x03",

            "#270F如果他一个人\x01",
            "不惹出什么麻烦就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x109,
        (
            "#1060F#5P嗨，没关系的。\x02\x03",

            "我可不觉得\x01",
            "那位小哥\x01",
            "有这么大能耐。\x02",
        )
    )

    Jump("loc_249D")

    label("loc_249D")

    CloseMessageWindow()
    Jump("loc_2624")

    label("loc_24A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2563")

    ChrTalk(    #45
        0x10B,
        (
            "#212F#5P这样好吗……？\x02\x03",

            "放着他这么一个人\x01",
            "不会又惹出什么乱子来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        (
            "#1060F#5P嗨，没关系的。\x02\x03",

            "怎么说也是『结社』的一员，\x01",
            "总该能照顾好自己吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2624")

    label("loc_2563")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2624")

    ChrTalk(    #47
        0x10E,
        (
            "#176F#5P……还真是有点担心呢。\x02\x03",

            "#178F他一个人别弄出\x01",
            "什么事来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        (
            "#1060F#5P嗨，没关系的。\x02\x03",

            "我可不觉得\x01",
            "那位小哥\x01",
            "有这么大能耐。\x02",
        )
    )

    Jump("loc_2623")

    label("loc_2623")

    CloseMessageWindow()

    label("loc_2624")


    ChrTalk(    #49
        0x10F,
        (
            "#1446F#5P……唉，\x01",
            "真是浪费时间。\x02\x03",

            "#1440F我们还是继续搜索王城吧。 \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2718)
    OP_28(0x2D, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_14AA end

    def Function_14_268A(): pass

    label("Function_14_268A")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFF8896, 0x2EE0, 0x159E6, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFA43E, 0x2EE0, 0x143D4, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFBECE, 0x36B0, 0x1322C, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFF844, 0x36B0, 0x1340C, 0x2710, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_14_268A end

    def Function_15_26EC(): pass

    label("Function_15_26EC")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_2749")

    label("loc_2749")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_15_26EC end

    def Function_16_2760(): pass

    label("Function_16_2760")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2836")
    OP_28(0x7, 0x4, 0x2)
    OP_82(0x82, 0x2)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2836")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05#40W　汝须将散发琥珀光辉之少年，\x01",
            "　　与坚定决意之公主一同\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_291E")
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291B")
    Call(0, 17)

    label("loc_291B")

    Jump("loc_291E")

    label("loc_291E")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_16_2760 end

    def Function_17_292A(): pass

    label("Function_17_292A")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)

    def lambda_2993():
        OP_6B(3540, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2993)
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

    # Function_17_292A end

    def Function_18_29E0(): pass

    label("Function_18_29E0")

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

    # Function_18_29E0 end

    SaveToFile()

Try(main)
