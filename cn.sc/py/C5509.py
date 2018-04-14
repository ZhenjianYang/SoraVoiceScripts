from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5509   ._SN',
        MapName             = 'Other',
        Location            = 'C5509.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 16,
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
        '匪兔',                                 # 9
        '目标',                                 # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12240 ._CH',             # 00
        'ED6_DT29/CH12241 ._CH',             # 01
        'ED6_DT29/CH12370 ._CH',             # 02
        'ED6_DT29/CH12371 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12270 ._CH',             # 06
        'ED6_DT29/CH12271 ._CH',             # 07
        'ED6_DT29/CH12372 ._CH',             # 08
        'ED6_DT27/CH04000 ._CH',             # 09
        'ED6_DT27/CH04001 ._CH',             # 0A
        'ED6_DT27/CH03005 ._CH',             # 0B
        'ED6_DT07/CH00420 ._CH',             # 0C
        'ED6_DT07/CH00421 ._CH',             # 0D
        'ED6_DT27/CH03095 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT29/CH12240P._CP',             # 00
        'ED6_DT29/CH12241P._CP',             # 01
        'ED6_DT29/CH12370P._CP',             # 02
        'ED6_DT29/CH12371P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12270P._CP',             # 06
        'ED6_DT29/CH12271P._CP',             # 07
        'ED6_DT29/CH12372P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04001P._CP',             # 0A
        'ED6_DT27/CH03005P._CP',             # 0B
        'ED6_DT07/CH00420P._CP',             # 0C
        'ED6_DT07/CH00421P._CP',             # 0D
        'ED6_DT27/CH03095P._CP',             # 0E
    )

    DeclNpc(
        X                   = 45840,
        Z                   = 0,
        Y                   = 183500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60000,
        Z                   = 500,
        Y                   = 183500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1EC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5380,
        Z                   = 0,
        Y                   = 37760,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 92320,
        Z                   = 0,
        Y                   = 33830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 92630,
        Z                   = 0,
        Y                   = 185930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 52700,
        Y                   = -1000,
        Z                   = 180050,
        Range               = 54740,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2D6A4,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -37300,
        TriggerZ            = 0,
        TriggerY            = 61450,
        TriggerRange        = 1000,
        ActorX              = -37910,
        ActorZ              = 0,
        ActorY              = 61450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20470,
        TriggerZ            = 0,
        TriggerY            = 67000,
        TriggerRange        = 1000,
        ActorX              = 20470,
        ActorZ              = 0,
        ActorY              = 67660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63940,
        TriggerZ            = 0,
        TriggerY            = 115470,
        TriggerRange        = 1000,
        ActorX              = 63940,
        ActorZ              = 0,
        ActorY              = 116130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63700,
        TriggerZ            = 0,
        TriggerY            = 77700,
        TriggerRange        = 1000,
        ActorX              = 63700,
        ActorZ              = 1300,
        ActorY              = 77700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119240,
        TriggerZ            = 250,
        TriggerY            = 123450,
        TriggerRange        = 1000,
        ActorX              = 119240,
        ActorZ              = 1550,
        ActorY              = 123450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 64050,
        TriggerZ            = 0,
        TriggerY            = 146260,
        TriggerRange        = 1000,
        ActorX              = 64050,
        ActorZ              = 1300,
        ActorY              = 146260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_2CD",          # 01, 1
        "Function_2_3F8",          # 02, 2
        "Function_3_40E",          # 03, 3
        "Function_4_525",          # 04, 4
        "Function_5_63C",          # 05, 5
        "Function_6_753",          # 06, 6
        "Function_7_A72",          # 07, 7
        "Function_8_B2A",          # 08, 8
        "Function_9_BEB",          # 09, 9
        "Function_10_C27",         # 0A, 10
        "Function_11_10AC",        # 0B, 11
        "Function_12_1135",        # 0C, 12
        "Function_13_1190",        # 0D, 13
        "Function_14_1191",        # 0E, 14
        "Function_15_1348",        # 0F, 15
        "Function_16_1359",        # 10, 16
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC")
    SetChrPos(0x8, 45840, 0, 183500, 90)
    ClearChrFlags(0x8, 0x80)

    label("loc_2CC")

    Return()

    # Function_0_2AE end

    def Function_1_2CD(): pass

    label("Function_1_2CD")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    OP_6F(0x11, 0)
    OP_70(0x11, 0x0)
    OP_6F(0x0, 0)
    Jump("loc_329")

    label("loc_306")

    OP_6F(0x11, 1)
    OP_70(0x11, 0x1)
    OP_6F(0x15, 30)
    OP_70(0x15, 0x1E)
    OP_6F(0x0, 30)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342")
    OP_6F(0x12, 0)
    OP_70(0x12, 0x0)
    Jump("loc_35E")

    label("loc_342")

    OP_6F(0x12, 1)
    OP_70(0x12, 0x1)
    OP_6F(0x13, 30)
    OP_70(0x13, 0x1E)

    label("loc_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377")
    OP_6F(0x10, 0)
    OP_70(0x10, 0x0)
    Jump("loc_393")

    label("loc_377")

    OP_6F(0x10, 1)
    OP_70(0x10, 0x1)
    OP_6F(0x14, 30)
    OP_70(0x14, 0x1E)

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5")
    OP_6F(0x1, 0)
    Jump("loc_3AC")

    label("loc_3A5")

    OP_6F(0x1, 30)

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE")
    OP_6F(0x16, 0)
    Jump("loc_3C5")

    label("loc_3BE")

    OP_6F(0x16, 60)

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7")
    OP_6F(0x17, 0)
    Jump("loc_3DE")

    label("loc_3D7")

    OP_6F(0x17, 60)

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0")
    OP_6F(0x18, 0)
    Jump("loc_3F7")

    label("loc_3F0")

    OP_6F(0x18, 60)

    label("loc_3F7")

    Return()

    # Function_1_2CD end

    def Function_2_3F8(): pass

    label("Function_2_3F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F8")

    label("loc_40D")

    Return()

    # Function_2_3F8 end

    def Function_3_40E(): pass

    label("Function_3_40E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_47D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1140)
    Jump("loc_4E3")

    label("loc_47D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_4E3")

    Jump("loc_517")

    label("loc_4E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_517")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_40E end

    def Function_4_525(): pass

    label("Function_4_525")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25B, 1)"), scpexpr(EXPR_END)), "loc_594")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x5B\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1141)
    Jump("loc_5FA")

    label("loc_594")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x5B\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5B\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_5FA")

    Jump("loc_62E")

    label("loc_5FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_62E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_525 end

    def Function_5_63C(): pass

    label("Function_5_63C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_6AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1142)
    Jump("loc_711")

    label("loc_6AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF5\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_711")

    Jump("loc_745")

    label("loc_714")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_745")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_63C end

    def Function_6_753(): pass

    label("Function_6_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22A, 0)), scpexpr(EXPR_END)), "loc_75B")
    Return()

    label("loc_75B")

    EventBegin(0x0)
    LoadEffect(0x0, "monster\\ms10180.eff")
    Fade(500)
    OP_6D(53680, 0, 184400, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 45840, 0, 183500, 90)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x9, 58000, 500, 183500, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 58660, 0, 184000, 270)
    SetChrPos(0x10A, 58660, 0, 183000, 270)

    def lambda_810():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_810)
    Sleep(150)

    def lambda_830():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_830)
    OP_0D()

    def lambda_84C():
        OP_6D(50080, 0, 184400, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_84C)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)

    def lambda_872():
        OP_99(0xFE, 0x0, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_872)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x14, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x14, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 0)

    def lambda_8C9():
        OP_96(0xFE, 0xCDBE, 0x0, 0x2D212, 0xC8, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C9)
    WaitChrThread(0x10A, 0x1)
    SetChrChipByIndex(0x10A, 14)
    SetChrSubChip(0x10A, 0)

    def lambda_8F6():
        OP_96(0xFE, 0xCEAE, 0x0, 0x2C70E, 0xC8, 0x2710)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8F6)
    PlayEffect(0x0, 0x1, 0x8, 1500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x9, 0, 0, 0, 0)

    def lambda_949():
        OP_9E(0xFE, 0x50, 0x0, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_949)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x10A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_83(0x1, 0x2)
    OP_44(0x8, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 7)
    Sleep(200)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Sleep(400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x10A, 12)
    SetChrSubChip(0x10A, 0)
    Sleep(1000)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x10A, 13)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x10A, 0x1000)

    def lambda_9DF():
        OP_8F(0xFE, 0xBBD0, 0x0, 0x2CD30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DF)

    def lambda_9FA():
        OP_8F(0xFE, 0xBBD0, 0x0, 0x2CC68, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9FA)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)

    def lambda_A23():
        OP_8F(0xFE, 0xC670, 0x0, 0x2CCCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A23)
    Sleep(400)
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_A5E"),
        (0, "loc_A63"),
        (2, "loc_A6A"),
        (SWITCH_DEFAULT, "loc_A71"),
    )


    label("loc_A5E")

    OP_B4(0x0)
    Jump("loc_A71")

    label("loc_A63")

    Call(0, 7)
    Jump("loc_A71")

    label("loc_A6A")

    Call(0, 8)
    Jump("loc_A71")

    label("loc_A71")

    Return()

    # Function_6_753 end

    def Function_7_A72(): pass

    label("Function_7_A72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(48940, 0, 183500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    SetChrPos(0x0, 48940, 0, 183500, 270)
    SetChrPos(0x1, 48940, 0, 183500, 270)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    OP_A2(0x1150)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_A72 end

    def Function_8_B2A(): pass

    label("Function_8_B2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    SetChrPos(0x8, 45840, 0, 183500, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(57100, 0, 183500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    SetChrPos(0x0, 57100, 0, 183500, 90)
    SetChrPos(0x1, 57100, 0, 183500, 90)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_B2A end

    def Function_9_BEB(): pass

    label("Function_9_BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA")
    Call(0, 10)
    Jump("loc_C26")

    label("loc_BFA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05门已经被打开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_C26")

    Return()

    # Function_9_BEB end

    def Function_10_C27(): pass

    label("Function_10_C27")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(41000, 0)
    SetChrPos(0x101, 64260, 0, 77280, 6)
    SetChrPos(0x10A, 63120, 0, 77280, 6)
    OP_69(0x101, 0x0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x1E)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x11, 1)
    OP_70(0x11, 0x1)
    Fade(1000)
    OP_6D(89570, 0, 79810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(100)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    Sleep(1500)
    OP_6D(64260, 0, 77280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_0D()
    Sleep(100)
    TurnDirection(0x101, 0x10A, 500)
    Sleep(500)

    ChrTalk(    #10
        0x101,
        (
            "#1019F什、什么啊，这个建筑……\x01",
            "为什么会有这样的装置！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #11
        0x10A,
        (
            "#818F大概是假想军事施设的\x01",
            "保安系统所制造而成的装置吧？\x02\x03",

            "潜入·逃出任务训练用的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1007F好、好奇怪的训练内容啊。\x01",
            "想起在雷斯顿要塞的时候了。\x02\x03",

            "#1015F先不说这个……\x01",
            "装置目前正在运作，\x01",
            "就代表这也是猎兵团干的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        (
            "#817F嗯，我想没错。\x02\x03",

            "#816F但是敌人也不可能\x01",
            "完全了解这个设施。\x02\x03",

            "谨慎沉稳地前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10A,
        (
            "#814F嗯？\x01",
            "怎么了，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1011F『谨慎沉稳』……\x01",
            "雪拉姐也说过同样的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#1315F嘿嘿……被你发现了？\x02\x03",

            "#810F嗯，我这是跟雪拉前辈现学现卖的。\x02\x03",

            "我在准游击士的时候\x01",
            "承蒙前辈的关照……\x02\x03",

            "但我的个性太浮躁，\x01",
            "所以经常被她像口头禅一样地念道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "感觉特别亲切呢。\x02\x03",

            "不只雪拉姐，\x01",
            "我也被约修亚这么说过……\x02\x03",

            "#1025F不过……\x01",
            "但现在只有我们两个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#1314F嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1006F走吧，亚妮拉丝。\x02\x03",

            "『谨慎沉稳』地行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        "#816F呵呵，明白啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1024)
    OP_28(0x80, 0x1, 0x800)
    EventEnd(0x0)
    Return()

    # Function_10_C27 end

    def Function_11_10AC(): pass

    label("Function_11_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1134")
    EventBegin(0x1)

    ChrTalk(    #22
        0x101,
        (
            "#1000F◆嗯～\x01",
            "这个光用手推\x01",
            "好像打不开呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#810F嗯，说得也是。\x02\x03",

            "一定有什么打开的方法才对。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1134")

    Return()

    # Function_11_10AC end

    def Function_12_1135(): pass

    label("Function_12_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1176")
    Sleep(100)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x12, 1)
    OP_70(0x12, 0x1)
    OP_A2(0x10AE)
    TalkEnd(0xFF)
    Jump("loc_118F")

    label("loc_1176")


    AnonymousTalk(    #24
        "\x07\x05电源已经开启。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFF)

    label("loc_118F")

    Return()

    # Function_12_1135 end

    def Function_13_1190(): pass

    label("Function_13_1190")

    Return()

    # Function_13_1190 end

    def Function_14_1191(): pass

    label("Function_14_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131B")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(41000, 0)
    SetChrPos(0x101, 64050, 0, 145340, 7)
    SetChrPos(0x10A, 62870, 0, 144720, 345)
    OP_69(0x101, 0x0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x14, 0)
    OP_70(0x14, 0x1E)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 6)), scpexpr(EXPR_END)), "loc_12DD")
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x10, 1)
    OP_70(0x10, 0x1)
    OP_A2(0x10AF)
    Fade(1000)
    OP_6D(89800, 0, 147350, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(100)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    Sleep(1500)
    OP_6D(64069, 0, 145340, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_0D()
    Sleep(100)

    ChrTalk(    #25
        0x101,
        "#1006F好，这样应该就行了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1025)
    EventEnd(0x0)
    Jump("loc_1318")

    label("loc_12DD")


    ChrTalk(    #26
        0x101,
        (
            "#1015F……咦？\x01",
            "好像没反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x14, 30)
    OP_70(0x14, 0x0)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    EventEnd(0x0)

    label("loc_1318")

    Jump("loc_1347")

    label("loc_131B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #27
        "\x07\x05门已经被打开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1347")

    Return()

    # Function_14_1191 end

    def Function_15_1348(): pass

    label("Function_15_1348")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(41000, 0)
    Return()

    # Function_15_1348 end

    def Function_16_1359(): pass

    label("Function_16_1359")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x416), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1366")
    Return()

    label("loc_1366")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_13FC")
    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #28
        (
            "\x07\x05认证组件已经启动了……\x01",
            "但好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_167A")

    label("loc_13FC")

    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05认证单元已经启动了……\x01",
            "但这个地方好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14AB")

    ChrTalk(    #30
        0x10A,
        (
            "#814F艾丝蒂尔。\x01",
            "好像不是这里哦。\x02\x03",

            "先往前走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    Jump("loc_1677")

    label("loc_14AB")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F1")

    ChrTalk(    #31
        0x10A,
        (
            "#812F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_14F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")

    ChrTalk(    #32
        0x10A,
        (
            "#813F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_152B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1563")

    ChrTalk(    #33
        0x10A,
        (
            "#814F这里好像\x01",
            "没什么可用的东西吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_1563")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(    #34
        0x10A,
        (
            "#817F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_159D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D7")

    ChrTalk(    #35
        0x10A,
        (
            "#818F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_15D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1609")

    ChrTalk(    #36
        0x10A,
        (
            "#819F嗯～看来\x01",
            "没找对地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_1609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1640")

    ChrTalk(    #37
        0x10A,
        (
            "#1315F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1674")

    label("loc_1640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #38
        0x10A,
        (
            "#1316F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1674")

    OP_A2(0x0)

    label("loc_1677")

    TalkEnd(0xFF)

    label("loc_167A")

    ClearMapFlags(0x80)
    Return()

    # Function_16_1359 end

    SaveToFile()

Try(main)
