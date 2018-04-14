from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2101.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60029",
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
        '玛诺利亚村方向',                       # 9
        '巴伦诺灯塔方向',                       # 10
        '古罗尼山道方向',                       # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH11060 ._CH',             # 0A
        'ED6_DT09/CH11061 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
        'ED6_DT29/CH12100 ._CH',             # 0E
        'ED6_DT29/CH12101 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH11060P._CP',             # 0A
        'ED6_DT09/CH11061P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
        'ED6_DT29/CH12100P._CP',             # 0E
        'ED6_DT29/CH12101P._CP',             # 0F
    )

    DeclNpc(
        X                   = 13030,
        Z                   = -2070,
        Y                   = -137400,
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

    DeclNpc(
        X                   = -72540,
        Z                   = -1880,
        Y                   = -134520,
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

    DeclNpc(
        X                   = -18980,
        Z                   = -2000,
        Y                   = 6950,
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
        X                   = -9560,
        Z                   = -2080,
        Y                   = -65670,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6390,
        Z                   = -2020,
        Y                   = -101440,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41930,
        Z                   = -1980,
        Y                   = -61650,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x170,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -75520,
        Z                   = -1990,
        Y                   = -83680,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x170,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -1970,
        TriggerY            = -43720,
        TriggerRange        = 1500,
        ActorX              = -16670,
        ActorZ              = -300,
        ActorY              = -43720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20680,
        TriggerZ            = -2009,
        TriggerY            = -44860,
        TriggerRange        = 1500,
        ActorX              = -20680,
        ActorZ              = -350,
        ActorY              = -44860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_243",          # 01, 1
        "Function_2_264",          # 02, 2
        "Function_3_2D0",          # 03, 3
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Return()

    # Function_0_242 end

    def Function_1_243(): pass

    label("Function_1_243")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFD0648, 0x23002C)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_243 end

    def Function_2_264(): pass

    label("Function_2_264")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05东　卢安市　　　３７４塞尔矩\x01",
            "　　玛诺利亚村　　６３塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_264 end

    def Function_3_2D0(): pass

    label("Function_3_2D0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05南　巴伦诺灯塔　　７０塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_2D0 end

    SaveToFile()

Try(main)
