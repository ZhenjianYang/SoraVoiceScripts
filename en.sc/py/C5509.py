from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Crybaby',                              # 9
        'Target',                               # 10
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
        "Function_4_560",          # 04, 4
        "Function_5_6C3",          # 05, 5
        "Function_6_83D",          # 06, 6
        "Function_7_B68",          # 07, 7
        "Function_8_C20",          # 08, 8
        "Function_9_CE1",          # 09, 9
        "Function_10_D28",         # 0A, 10
        "Function_11_144C",        # 0B, 11
        "Function_12_14F9",        # 0C, 12
        "Function_13_1566",        # 0D, 13
        "Function_14_1567",        # 0E, 14
        "Function_15_173E",        # 0F, 15
        "Function_16_174F",        # 10, 16
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

    OP_EA(0x2, 0x96, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_47F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1140)
    Jump("loc_4E3")

    label("loc_47F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_4E3")

    Jump("loc_552")

    label("loc_4E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You've looted this chest already.\x01",
            "It's strange...it almost feels heavier now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_552")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_40E end

    def Function_4_560(): pass

    label("Function_4_560")

    OP_EA(0x2, 0x97, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25B, 1)"), scpexpr(EXPR_END)), "loc_5D1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x5B\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1141)
    Jump("loc_635")

    label("loc_5D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x5B\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5B\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_635")

    Jump("loc_6B5")

    label("loc_638")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05As you close the chest, it gives you a sad look.\x01",
            "It wishes it had something more for you, too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_560 end

    def Function_5_6C3(): pass

    label("Function_5_6C3")

    OP_EA(0x2, 0x98, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_734")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1142)
    Jump("loc_798")

    label("loc_734")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_798")

    Jump("loc_82F")

    label("loc_79B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You know the chest is empty, but it has\x01",
            "served you well. Instead of opening it, you give\x01",
            "it a gentle pat on the head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_82F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6C3 end

    def Function_6_83D(): pass

    label("Function_6_83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22A, 0)), scpexpr(EXPR_END)), "loc_845")
    Return()

    label("loc_845")

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

    def lambda_8FA():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FA)
    Sleep(150)

    def lambda_91A():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_91A)
    OP_0D()

    def lambda_936():
        OP_6D(50080, 0, 184400, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_936)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)

    def lambda_95C():
        OP_99(0xFE, 0x0, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_95C)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x14, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x14, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 0)

    def lambda_9B3():
        OP_96(0xFE, 0xCDBE, 0x0, 0x2D212, 0xC8, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B3)
    WaitChrThread(0x10A, 0x1)
    SetChrChipByIndex(0x10A, 14)
    SetChrSubChip(0x10A, 0)

    def lambda_9E0():
        OP_96(0xFE, 0xCEAE, 0x0, 0x2C70E, 0xC8, 0x2710)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9E0)
    PlayEffect(0x0, 0x1, 0x8, 1500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x9, 0, 0, 0, 0)

    def lambda_A33():
        OP_9E(0xFE, 0x50, 0x0, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A33)
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

    def lambda_AC9():
        OP_8F(0xFE, 0xBBD0, 0x0, 0x2CD30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC9)

    def lambda_AE4():
        OP_8F(0xFE, 0xBBD0, 0x0, 0x2CC68, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_AE4)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)

    def lambda_B0D():
        OP_8F(0xFE, 0xC670, 0x0, 0x2CCCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0D)
    Sleep(400)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x8, 0x1)
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_B54"),
        (0, "loc_B59"),
        (2, "loc_B60"),
        (SWITCH_DEFAULT, "loc_B67"),
    )


    label("loc_B54")

    OP_B4(0x0)
    Jump("loc_B67")

    label("loc_B59")

    Call(0, 7)
    Jump("loc_B67")

    label("loc_B60")

    Call(0, 8)
    Jump("loc_B67")

    label("loc_B67")

    Return()

    # Function_6_83D end

    def Function_7_B68(): pass

    label("Function_7_B68")

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
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    OP_A2(0x1150)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_B68 end

    def Function_8_C20(): pass

    label("Function_8_C20")

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
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_C20 end

    def Function_9_CE1(): pass

    label("Function_9_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF0")
    Call(0, 10)
    Jump("loc_D27")

    label("loc_CF0")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05The gate is already open.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_D27")

    Return()

    # Function_9_CE1 end

    def Function_10_D28(): pass

    label("Function_10_D28")

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
            "#1019F#4PWhat the heck is with this building...?\x01",
            "Fake walls and weird gimmicks...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #11
        0x10A,
        (
            "#818FHmm... Don't you find this sort of stuff in\x01",
            "military bases, as a security thingy?\x01",
            "Y'know, a movable wall?\x02\x03",

            "I guess this place really is used for,\x01",
            "like, infiltration or escape training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1007F#4PA military-themed course? Aw, great.\x01",
            "It's like I'm trapped in Leiston Fortress\x01",
            "all over again.\x02\x03",

            "#1015FBut anyway... I suppose if this thing is\x01",
            "active, the jaegers are in the building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        (
            "#817FYeah, I'd say it's a good bet.\x02\x03",

            "#816FGood news is, our enemies probably don't\x01",
            "know this place any better than we do.\x02\x03",

            "If we proceed carefully and deliberately,\x01",
            "we should be cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10A,
        (
            "#814FHm? What's wrong, Estelle?\x01",
            "Did I say something bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1011F#4P'Carefully and deliberately...'\x01",
            "I remember Schera always telling\x01",
            "me the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#1315FHaha! Whoops, my dark, horrible past is exposed!\x02\x03",

            "#810FYeah, that's something Schera\x01",
            "used to tell me a lot.\x02\x03",

            "She was my mentor for a while when\x01",
            "I was still a newbie, you see...\x02\x03",

            "And, well, I was kind of a super-scatterbrain.\x01",
            "I heard that line so much, though, it\x01",
            "eventually got burned into my skull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1016F#4PHa ha... Haaaa...\x01",
            "Yeeeah, I've got a pretty good\x01",
            "idea of what you mean.\x02\x03",

            "Joshua was just as fond of that\x01",
            "saying as Schera was...\x02\x03",

            "#1025FBut...neither of them are here\x01",
            "now, huh? It's just us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#1314FYeah... It's all on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1006F#4PLet's go, Anelace.\x02\x03",

            "Carefully and deliberately, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        "#816FMaybe even deliberately and carefully!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1024)
    OP_28(0x80, 0x1, 0x800)
    EventEnd(0x0)
    Return()

    # Function_10_D28 end

    def Function_11_144C(): pass

    label("Function_11_144C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F8")
    EventBegin(0x1)

    ChrTalk(    #22
        0x101,
        (
            "#1000F◆う～ん、\x01",
            "これは手で押したくらいじゃ\x01",
            "開きそうにないわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#810Fうん、そうだね。\x02\x03",

            "きっと何か、開く方法があるはずだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_14F8")

    Return()

    # Function_11_144C end

    def Function_12_14F9(): pass

    label("Function_12_14F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153A")
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
    Jump("loc_1565")

    label("loc_153A")


    AnonymousTalk(    #24
        "\x07\x05Orbal energy is already flowing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFF)

    label("loc_1565")

    Return()

    # Function_12_14F9 end

    def Function_13_1566(): pass

    label("Function_13_1566")

    Return()

    # Function_13_1566 end

    def Function_14_1567(): pass

    label("Function_14_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1706")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 6)), scpexpr(EXPR_END)), "loc_16C4")
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
        "#1006FOkay, it looks like this should work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1025)
    EventEnd(0x0)
    Jump("loc_1703")

    label("loc_16C4")


    ChrTalk(    #26
        0x101,
        "#1015F...Huh? It's not working.\x02",
    )

    CloseMessageWindow()
    OP_6F(0x14, 30)
    OP_70(0x14, 0x0)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    EventEnd(0x0)

    label("loc_1703")

    Jump("loc_173D")

    label("loc_1706")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #27
        "\x07\x05The gate is already open.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_173D")

    Return()

    # Function_14_1567 end

    def Function_15_173E(): pass

    label("Function_15_173E")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(41000, 0)
    Return()

    # Function_15_173E end

    def Function_16_174F(): pass

    label("Function_16_174F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x416), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175C")
    Return()

    label("loc_175C")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_17FA")
    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #28
        "\x07\x05Activated ID Unit, but...there was no notable response.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_1AE3")

    label("loc_17FA")

    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05Activated ID Unit, but...there was no notable response\x01",
            "to this location.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18DD")

    ChrTalk(    #30
        0x10A,
        (
            "#814FEstelle, I don't think this is the right place.\x02\x03",

            "Let's just keep going, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    Jump("loc_1AE0")

    label("loc_18DD")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")

    ChrTalk(    #31
        0x10A,
        "#812FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_192A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #32
        0x10A,
        "#813FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_196B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A6")

    ChrTalk(    #33
        0x10A,
        "#814FMaybe you use it somewhere else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_19A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E7")

    ChrTalk(    #34
        0x10A,
        "#817FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_19E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A28")

    ChrTalk(    #35
        0x10A,
        "#818FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_1A28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5C")

    ChrTalk(    #36
        0x10A,
        "#819FSeems like this isn't it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A9E")

    ChrTalk(    #37
        0x10A,
        "#1315FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ADD")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(    #38
        0x10A,
        "#1316FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()

    label("loc_1ADD")

    OP_A2(0x0)

    label("loc_1AE0")

    TalkEnd(0xFF)

    label("loc_1AE3")

    ClearMapFlags(0x80)
    Return()

    # Function_16_174F end

    SaveToFile()

Try(main)
