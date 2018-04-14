from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1100   ._SN',
        MapName             = 'Bose',
        Location            = 'R1100.x',
        MapIndex            = 55,
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
        '威尔特桥·关所方向',                   # 9
        '柏斯方向',                             # 10
        '迷雾峡谷方向',                         # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10310 ._CH',             # 02
        'ED6_DT09/CH10311 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
        'ED6_DT09/CH10350 ._CH',             # 08
        'ED6_DT09/CH10351 ._CH',             # 09
        'ED6_DT09/CH10540 ._CH',             # 0A
        'ED6_DT09/CH10541 ._CH',             # 0B
        'ED6_DT09/CH10550 ._CH',             # 0C
        'ED6_DT09/CH10551 ._CH',             # 0D
        'ED6_DT09/CH10870 ._CH',             # 0E
        'ED6_DT09/CH10871 ._CH',             # 0F
        'ED6_DT09/CH10900 ._CH',             # 10
        'ED6_DT09/CH10901 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10310P._CP',             # 02
        'ED6_DT09/CH10311P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
        'ED6_DT09/CH10350P._CP',             # 08
        'ED6_DT09/CH10351P._CP',             # 09
        'ED6_DT09/CH10540P._CP',             # 0A
        'ED6_DT09/CH10541P._CP',             # 0B
        'ED6_DT09/CH10550P._CP',             # 0C
        'ED6_DT09/CH10551P._CP',             # 0D
        'ED6_DT09/CH10870P._CP',             # 0E
        'ED6_DT09/CH10871P._CP',             # 0F
        'ED6_DT09/CH10900P._CP',             # 10
        'ED6_DT09/CH10901P._CP',             # 11
    )

    DeclNpc(
        X                   = 212420,
        Z                   = 0,
        Y                   = -31840,
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
        X                   = 46200,
        Z                   = 0,
        Y                   = -11050,
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
        X                   = 104100,
        Z                   = -100,
        Y                   = 66730,
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
        X                   = 154130,
        Z                   = 30,
        Y                   = -20040,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 138560,
        Z                   = 0,
        Y                   = -700,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 127250,
        Z                   = 50,
        Y                   = 16710,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 81200,
        Z                   = 0,
        Y                   = 10930,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 80560,
        Z                   = 0,
        Y                   = -8189,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 115320,
        Z                   = -30,
        Y                   = 7050,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 101320,
        TriggerZ            = 0,
        TriggerY            = 18640,
        TriggerRange        = 1500,
        ActorX              = 101320,
        ActorZ              = 1300,
        ActorY              = 18640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_267",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_290",          # 03, 3
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Return()

    # Function_0_266 end

    def Function_1_267(): pass

    label("Function_1_267")

    OP_16(0x2, 0xFA0, 0x0, 0xFFFE1F88, 0x230015)
    Return()

    # Function_1_267 end

    def Function_2_27A(): pass

    label("Function_2_27A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_27A")

    label("loc_28F")

    Return()

    # Function_2_27A end

    def Function_3_290(): pass

    label("Function_3_290")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05北　迷雾峡谷\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_290 end

    SaveToFile()

Try(main)
