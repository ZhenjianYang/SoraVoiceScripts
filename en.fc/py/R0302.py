from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0302   ._SN',
        MapName             = 'rolent',
        Location            = 'R0302.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R0302   ._SN',
            'ED6_DT01/R0302_1 ._SN',
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
        'Monster',                              # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Rolent',                               # 14
        'Malga Mine',                           # 15
        '赤茶玉虫',                             # 16
        'リリームーバー',                       # 17
        '赤茶玉虫',                             # 18
        'リリームーバー',                       # 19
        '赤茶玉虫',                             # 20
        'リリームーバー',                       # 21
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00110 ._CH',             # 03
        'ED6_DT09/CH10020 ._CH',             # 04
        'ED6_DT09/CH10021 ._CH',             # 05
        'ED6_DT09/CH10180 ._CH',             # 06
        'ED6_DT09/CH10181 ._CH',             # 07
        'ED6_DT09/CH10260 ._CH',             # 08
        'ED6_DT09/CH10261 ._CH',             # 09
        'ED6_DT09/CH10210 ._CH',             # 0A
        'ED6_DT09/CH10211 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00110P._CP',             # 03
        'ED6_DT09/CH10020P._CP',             # 04
        'ED6_DT09/CH10021P._CP',             # 05
        'ED6_DT09/CH10180P._CP',             # 06
        'ED6_DT09/CH10181P._CP',             # 07
        'ED6_DT09/CH10260P._CP',             # 08
        'ED6_DT09/CH10261P._CP',             # 09
        'ED6_DT09/CH10210P._CP',             # 0A
        'ED6_DT09/CH10211P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -146110,
        Z                   = 10,
        Y                   = -9950,
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
        X                   = -163040,
        Z                   = 3920,
        Y                   = 102800,
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
        X                   = -156000,
        Z                   = 2000,
        Y                   = 18000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x71,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -146000,
        Z                   = 2100,
        Y                   = 27000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x69,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -130000,
        Z                   = 4100,
        Y                   = 26000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -117000,
        Z                   = 4100,
        Y                   = 31000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x73,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154000,
        Z                   = 2000,
        Y                   = 47000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -156000,
        Z                   = 4000,
        Y                   = 68000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x76,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -158700,
        Y                   = 3500,
        Z                   = 94900,
        Range               = -166600,
        Unknown_10          = 0x1BBC,
        Unknown_14          = 0x16F30,
        Unknown_18          = 0x10000,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = -109910,
        TriggerZ            = 5850,
        TriggerY            = 62020,
        TriggerRange        = 1000,
        ActorX              = -109910,
        ActorZ              = 7350,
        ActorY              = 62020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -113700,
        TriggerZ            = 5930,
        TriggerY            = 66620,
        TriggerRange        = 1500,
        ActorX              = -113700,
        ActorZ              = 5930,
        ActorY              = 66620,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FA",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_370",          # 02, 2
        "Function_3_386",          # 03, 3
    )


    def Function_0_2FA(): pass

    label("Function_0_2FA")

    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    Return()

    # Function_0_2FA end

    def Function_1_314(): pass

    label("Function_1_314")

    OP_16(0x2, 0xFA0, 0xFFFBF0F0, 0xFFFEB010, 0x30010)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x0, 0)
    Jump("loc_33F")

    label("loc_338")

    OP_6F(0x0, 60)

    label("loc_33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_358")
    OP_64(0x1, 0x1)
    Jump("loc_36F")

    label("loc_358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36F")
    OP_64(0x1, 0x1)
    Jump("loc_36F")

    label("loc_36F")

    Return()

    # Function_1_314 end

    def Function_2_370(): pass

    label("Function_2_370")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_370")

    label("loc_385")

    Return()

    # Function_2_370 end

    def Function_3_386(): pass

    label("Function_3_386")

    SetMapFlags(0x8000000)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x132, 1)"), scpexpr(EXPR_END)), "loc_401")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00Found \x07\x02White Bracelet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x21B)
    Jump("loc_481")

    label("loc_401")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00Found \x07\x02White Bracelet\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02White Bracelet\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_481")

    Jump("loc_4CF")

    label("loc_484")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        "\x07\x05This chest is now full of disappointment...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x7C)

    label("loc_4CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_386 end

    SaveToFile()

Try(main)
