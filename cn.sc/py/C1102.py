from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1102   ._SN',
        MapName             = 'Bose',
        Location            = 'C1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C1102_1 ._SN',
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
        '强化猎兵',                             # 9
        '强化猎兵',                             # 10
        '哨兵',                                 # 11
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
        'ED6_DT07/CH00162 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT09/CH10300 ._CH',             # 02
        'ED6_DT09/CH10301 ._CH',             # 03
        'ED6_DT27/CH03610 ._CH',             # 04
        'ED6_DT27/CH03750 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12570 ._CH',             # 08
        'ED6_DT29/CH12571 ._CH',             # 09
        'ED6_DT29/CH12574 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00162P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT09/CH10300P._CP',             # 02
        'ED6_DT09/CH10301P._CP',             # 03
        'ED6_DT27/CH03610P._CP',             # 04
        'ED6_DT27/CH03750P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12570P._CP',             # 08
        'ED6_DT29/CH12571P._CP',             # 09
        'ED6_DT29/CH12574P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -29330,
        Z                   = -500,
        Y                   = 36850,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6698,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -84750,
        Z                   = -410,
        Y                   = 68560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6699,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50700,
        Z                   = 0,
        Y                   = 57550,
        Unknown_0C          = 225,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6700,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 49810,
        Z                   = 0,
        Y                   = 10380,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6701,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75930,
        Z                   = -500,
        Y                   = 185910,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAD,
        Unknown_18          = 6702,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -46900,
        Y                   = -2000,
        Z                   = 26000,
        Range               = -46100,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x7530,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = 7410,
        TriggerZ            = 0,
        TriggerY            = 43900,
        TriggerRange        = 1000,
        ActorX              = 6750,
        ActorZ              = 0,
        ActorY              = 43900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -75700,
        TriggerZ            = 0,
        TriggerY            = 30920,
        TriggerRange        = 1000,
        ActorX              = -75080,
        ActorZ              = 0,
        ActorY              = 30400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -89670,
        TriggerZ            = -250,
        TriggerY            = 78010,
        TriggerRange        = 1000,
        ActorX              = -90330,
        ActorZ              = -250,
        ActorY              = 78140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80220,
        TriggerZ            = -250,
        TriggerY            = 76890,
        TriggerRange        = 1000,
        ActorX              = -79560,
        ActorZ              = -250,
        ActorY              = 76890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41820,
        TriggerZ            = -250,
        TriggerY            = 99770,
        TriggerRange        = 1000,
        ActorX              = -41820,
        ActorZ              = -250,
        ActorY              = 99110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28930,
        TriggerZ            = -130,
        TriggerY            = 47490,
        TriggerRange        = 1000,
        ActorX              = -28930,
        ActorZ              = 1500,
        ActorY              = 47490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -69290,
        TriggerZ            = 0,
        TriggerY            = 170530,
        TriggerRange        = 1000,
        ActorX              = -69860,
        ActorZ              = 0,
        ActorY              = 170530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_3C7",          # 01, 1
        "Function_2_4F6",          # 02, 2
        "Function_3_60D",          # 03, 3
        "Function_4_724",          # 04, 4
        "Function_5_83B",          # 05, 5
        "Function_6_952",          # 06, 6
        "Function_7_A69",          # 07, 7
        "Function_8_B80",          # 08, 8
        "Function_9_B8C",          # 09, 9
        "Function_10_CA2",         # 0A, 10
        "Function_11_110E",        # 0B, 11
        "Function_12_131A",        # 0C, 12
        "Function_13_1417",        # 0D, 13
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_362")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_346")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_362")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_362")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(1, 1)

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392")
    ClearChrFlags(0xB, 0x80)

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F")
    ClearChrFlags(0xC, 0x80)

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC")
    ClearChrFlags(0xD, 0x80)

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    ClearChrFlags(0xE, 0x80)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    ClearChrFlags(0xF, 0x80)

    label("loc_3C6")

    Return()

    # Function_0_30A end

    def Function_1_3C7(): pass

    label("Function_1_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9")
    OP_6F(0x0, 0)
    Jump("loc_3E0")

    label("loc_3D9")

    OP_6F(0x0, 60)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2")
    OP_6F(0x1, 0)
    Jump("loc_3F9")

    label("loc_3F2")

    OP_6F(0x1, 60)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B")
    OP_6F(0x2, 0)
    Jump("loc_412")

    label("loc_40B")

    OP_6F(0x2, 60)

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424")
    OP_6F(0x3, 0)
    Jump("loc_42B")

    label("loc_424")

    OP_6F(0x3, 60)

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D")
    OP_6F(0x4, 0)
    Jump("loc_444")

    label("loc_43D")

    OP_6F(0x4, 60)

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x367, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456")
    OP_6F(0x6, 0)
    Jump("loc_45D")

    label("loc_456")

    OP_6F(0x6, 60)

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_468")
    OP_64(0x5, 0x1)

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B4")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_1B(0x4, 0x0, 0xD)
    Jump("loc_4B4")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_4B4")

    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F5")
    Event(1, 0)

    label("loc_4F5")

    Return()

    # Function_1_3C7 end

    def Function_2_4F6(): pass

    label("Function_2_4F6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_565")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B33)
    Jump("loc_5CB")

    label("loc_565")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_5CB")

    Jump("loc_5FF")

    label("loc_5CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5FF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_4F6 end

    def Function_3_60D(): pass

    label("Function_3_60D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_67C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B34)
    Jump("loc_6E2")

    label("loc_67C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6E2")

    Jump("loc_716")

    label("loc_6E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_716")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_60D end

    def Function_4_724(): pass

    label("Function_4_724")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D7, 1)"), scpexpr(EXPR_END)), "loc_793")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xD7\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B35)
    Jump("loc_7F9")

    label("loc_793")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xD7\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD7\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_7F9")

    Jump("loc_82D")

    label("loc_7FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_82D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_724 end

    def Function_5_83B(): pass

    label("Function_5_83B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_8AA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B36)
    Jump("loc_910")

    label("loc_8AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_910")

    Jump("loc_944")

    label("loc_913")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_944")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_83B end

    def Function_6_952(): pass

    label("Function_6_952")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AA, 1)"), scpexpr(EXPR_END)), "loc_9C1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xAA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B37)
    Jump("loc_A27")

    label("loc_9C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xAA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xAA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A27")

    Jump("loc_A5B")

    label("loc_A2A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A5B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_952 end

    def Function_7_A69(): pass

    label("Function_7_A69")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x367, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B41")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15C, 1)"), scpexpr(EXPR_END)), "loc_AD8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x5C\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B38)
    Jump("loc_B3E")

    label("loc_AD8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x5C\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5C\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_B3E")

    Jump("loc_B72")

    label("loc_B41")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B72")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A69 end

    def Function_8_B80(): pass

    label("Function_8_B80")

    EventBegin(0x0)
    NewScene("ED6_DT21/C1103   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_8_B80 end

    def Function_9_B8C(): pass

    label("Function_9_B8C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9F")
    Call(0, 12)

    label("loc_B9F")

    OP_6D(1020, 0, 6630, 0)
    OP_67(0, 8740, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 430, 0, 6420, 0)
    SetChrPos(0x107, 1480, 0, 6290, 0)
    SetChrPos(0xF8, -160, 0, 5280, 0)
    SetChrPos(0xF9, 1570, 0, 5060, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x107,
        "#065F#5P阿、阿加特哥哥的声音！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002F这个响声的方向\x01",
            "似乎来自露天采掘场。\x02\x03",

            "#1005F总之赶快去吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_B8C end

    def Function_10_CA2(): pass

    label("Function_10_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C9")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD0")
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_CD0")

    Fade(1000)
    OP_6D(-29880, -430, 46640, 0)
    OP_67(0, 10510, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -29170, -500, 45850, 0)
    SetChrPos(0x107, -30200, -500, 45730, 0)
    SetChrPos(0xF8, -30290, -500, 44420, 0)
    SetChrPos(0xF9, -29090, -500, 44350, 0)
    OP_0D()

    ChrTalk(    #20
        0x101,
        "#1020F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        "#065F#6P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1020F这里原本可以通往\x01",
            "外面的露天采掘场才对……\x02\x03",

            "怎么被岩石堵住了！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(    #23
        0x105,
        (
            "#043F#6P搞不好，是龙发飙\x01",
            "造成崩塌也不一定……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9B")

    label("loc_E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5A")

    ChrTalk(    #24
        0x103,
        (
            "#022F#6P搞不好，是龙发飙\x01",
            "造成崩塌也不一定呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9B")

    label("loc_E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(    #25
        0x104,
        (
            "#035F#6P搞不好，是龙发飙\x01",
            "造成崩塌也不一定啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B")


    ChrTalk(    #26
        0x107,
        (
            "#062F#6P那，那就\x01",
            "用我的导力炮！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 0)
    OP_0D()
    Sleep(500)

    def lambda_EE0():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE0)
    Sleep(100)

    def lambda_EF3():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_EF3)
    Sleep(10)
    TurnDirection(0xF8, 0x107, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F57")

    ChrTalk(    #27
        0x108,
        (
            "#072F#6P不，最好不要。\x02\x03",

            "随便使其振动\x01",
            "搞不好会塌得更厉害。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFE")

    label("loc_F57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAB")

    ChrTalk(    #28
        0x104,
        (
            "#032F#6P不，最好不要吧。\x02\x03",

            "随便使其振动\x01",
            "搞不好会坍塌得更厉害。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFE")

    label("loc_FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFE")

    ChrTalk(    #29
        0x103,
        (
            "#022F#6P不，最好不要哦。\x02\x03",

            "随便使其振动\x01",
            "搞不好会坍塌得更厉害吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFE")

    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #30
        0x107,
        "#561F#6P啊、啊呜……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(300)

    ChrTalk(    #31
        0x101,
        (
            "#1002F#4P提妲……\x01",
            "我明白你的心情，不过镇定点。\x02\x03",

            "总之先寻找别的途径吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #32
        0x107,
        "#062F#5P嗯、嗯……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A18)
    OP_28(0x94, 0x1, 0x20)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_110D")

    label("loc_10C9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05出口被岩石堵住了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_110D")

    Return()

    # Function_10_CA2 end

    def Function_11_110E(): pass

    label("Function_11_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 1)), scpexpr(EXPR_END)), "loc_1116")
    Return()

    label("loc_1116")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1137")
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_1137")

    Fade(1000)
    OP_6D(-48350, 50, 28560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -47490, 50, 28410, 270)
    SetChrPos(0x107, -47470, 50, 27380, 270)
    SetChrPos(0xF8, -46180, 50, 28740, 270)
    SetChrPos(0xF9, -45960, 0, 27320, 270)
    OP_0D()

    ChrTalk(    #34
        0x101,
        (
            "#1004F#6P咦……\x02\x03",

            "这里的桥，之前来的时候\x01",
            "好像是坏掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125B")

    ChrTalk(    #35
        0x103,
        (
            "#022F#6P记得听说空贼事件以后，\x01",
            "军方把它修复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1015F#6P这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1309")

    label("loc_125B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(    #37
        0x105,
        (
            "#042F#6P搞不好是王国军\x01",
            "修复了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1015F#6P原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1309")

    label("loc_12B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(    #39
        0x104,
        (
            "#035F#6P唔，搞不好\x01",
            "是军队修复了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1015F原来如此……\x02",
    )

    CloseMessageWindow()

    label("loc_1309")

    OP_A2(0x1A19)
    OP_28(0x94, 0x1, 0x40)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_110E end

    def Function_12_131A(): pass

    label("Function_12_131A")

    FadeToDark(0, 0, -1)
    OP_6D(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13D1"),
        (1, "loc_13D7"),
        (SWITCH_DEFAULT, "loc_13DD"),
    )


    label("loc_13D1")

    OP_A2(0x1200)
    Jump("loc_13DD")

    label("loc_13D7")

    OP_A2(0x1201)
    Jump("loc_13DD")

    label("loc_13DD")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_131A end

    def Function_13_1417(): pass

    label("Function_13_1417")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1457")

    ChrTalk(    #41
        0x101,
        (
            "#1002F阿加特就在里面……\x01",
            "总之现在赶快吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_1457")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148C")

    ChrTalk(    #42
        0x103,
        (
            "#022F阿加特就在里面。\x01",
            "赶快去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_148C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C1")

    ChrTalk(    #43
        0x105,
        (
            "#042F阿加特就在里面。\x01",
            "赶快去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_14C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(    #44
        0x104,
        (
            "#032F阿加特就在里面。\x01",
            "赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_14F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")

    ChrTalk(    #45
        0x107,
        (
            "#065F阿加特就在里面……\x01",
            "要、要赶快才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_1533")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(    #46
        0x108,
        (
            "#072F阿加特就在里面。\x01",
            "总之这就赶快前进吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156F")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_1417 end

    SaveToFile()

Try(main)
