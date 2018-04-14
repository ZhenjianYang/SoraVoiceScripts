from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5502   ._SN',
        MapName             = 'Other',
        Location            = 'C5502.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '',                                     # 9
        '',                                     # 10
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
        'ED6_DT29/CH12190 ._CH',             # 00
        'ED6_DT29/CH12191 ._CH',             # 01
        'ED6_DT29/CH12200 ._CH',             # 02
        'ED6_DT29/CH12201 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12220 ._CH',             # 06
        'ED6_DT29/CH12221 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12190P._CP',             # 00
        'ED6_DT29/CH12191P._CP',             # 01
        'ED6_DT29/CH12200P._CP',             # 02
        'ED6_DT29/CH12201P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12220P._CP',             # 06
        'ED6_DT29/CH12221P._CP',             # 07
    )

    DeclNpc(
        X                   = -47360,
        Z                   = -1000,
        Y                   = 191570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 12820,
        Z                   = 0,
        Y                   = 136490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27240,
        Z                   = 0,
        Y                   = 139530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42600,
        Z                   = 0,
        Y                   = 150280,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39260,
        Z                   = 0,
        Y                   = 169730,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28360,
        Z                   = 0,
        Y                   = 190270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14670,
        Z                   = 0,
        Y                   = 176940,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32659,
        Z                   = -2000,
        Y                   = 160510,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18800,
        Z                   = -2000,
        Y                   = 167080,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43100,
        Z                   = -2000,
        Y                   = 155530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1160,
        TriggerZ            = 0,
        TriggerY            = 144370,
        TriggerRange        = 1700,
        ActorX              = -1160,
        ActorZ              = 2500,
        ActorY              = 144370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 169110,
        TriggerRange        = 1700,
        ActorX              = -13210,
        ActorZ              = 2500,
        ActorY              = 169110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4340,
        TriggerZ            = 0,
        TriggerY            = 181980,
        TriggerRange        = 1700,
        ActorX              = 4340,
        ActorZ              = 2500,
        ActorY              = 181980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30880,
        TriggerZ            = 0,
        TriggerY            = 150510,
        TriggerRange        = 1700,
        ActorX              = -30880,
        ActorZ              = 2500,
        ActorY              = 150510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38950,
        TriggerZ            = 0,
        TriggerY            = 173800,
        TriggerRange        = 1000,
        ActorX              = -38990,
        ActorZ              = 0,
        ActorY              = 174460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42500,
        TriggerZ            = 0,
        TriggerY            = 173790,
        TriggerRange        = 1000,
        ActorX              = -42500,
        ActorZ              = 0,
        ActorY              = 174410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35450,
        TriggerZ            = 0,
        TriggerY            = 173790,
        TriggerRange        = 1000,
        ActorX              = -35450,
        ActorZ              = 0,
        ActorY              = 174450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36970,
        TriggerZ            = 0,
        TriggerY            = 187560,
        TriggerRange        = 1000,
        ActorX              = -36880,
        ActorZ              = 0,
        ActorY              = 186860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11070,
        TriggerZ            = 0,
        TriggerY            = 155530,
        TriggerRange        = 1000,
        ActorX              = 11070,
        ActorZ              = 0,
        ActorY              = 154910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -7710,
        TriggerZ            = 0,
        TriggerY            = 158960,
        TriggerRange        = 1000,
        ActorX              = -7050,
        ActorZ              = 0,
        ActorY              = 158960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47400,
        TriggerZ            = -2000,
        TriggerY            = 190910,
        TriggerRange        = 1000,
        ActorX              = -47360,
        ActorZ              = -2000,
        ActorY              = 191570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_393",          # 01, 1
        "Function_2_50D",          # 02, 2
        "Function_3_523",          # 03, 3
        "Function_4_68D",          # 04, 4
        "Function_5_7D2",          # 05, 5
        "Function_6_8E9",          # 06, 6
        "Function_7_A00",          # 07, 7
        "Function_8_B17",          # 08, 8
        "Function_9_C2E",          # 09, 9
        "Function_10_DFE",         # 0A, 10
        "Function_11_F9D",         # 0B, 11
        "Function_12_113C",        # 0C, 12
        "Function_13_12DB",        # 0D, 13
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Return()

    # Function_0_392 end

    def Function_1_393(): pass

    label("Function_1_393")

    OP_22(0x1C7, 0x0, 0x64)
    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    OP_72(0x5, 0x28)
    OP_72(0x6, 0x28)
    OP_72(0x7, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_END)), "loc_3D5")
    OP_6F(0x1, 120)
    OP_6F(0x6, 60)

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_END)), "loc_3EA")
    OP_6F(0x1, 120)
    OP_6F(0x6, 160)

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_END)), "loc_3FF")
    OP_6F(0x3, 120)
    OP_6F(0x2, 60)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_END)), "loc_414")
    OP_6F(0x3, 120)
    OP_6F(0x2, 160)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_END)), "loc_429")
    OP_6F(0x4, 120)
    OP_6F(0x5, 60)

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_END)), "loc_43E")
    OP_6F(0x4, 120)
    OP_6F(0x5, 160)

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 5)), scpexpr(EXPR_END)), "loc_453")
    OP_6F(0x7, 60)
    OP_6F(0x0, 260)

    label("loc_453")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F")
    OP_6F(0x8, 0)
    Jump("loc_476")

    label("loc_46F")

    OP_6F(0x8, 60)

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488")
    OP_6F(0x9, 0)
    Jump("loc_48F")

    label("loc_488")

    OP_6F(0x9, 60)

    label("loc_48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    OP_6F(0xA, 0)
    Jump("loc_4A8")

    label("loc_4A1")

    OP_6F(0xA, 60)

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_6F(0xB, 0)
    Jump("loc_4C1")

    label("loc_4BA")

    OP_6F(0xB, 60)

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    OP_6F(0xC, 0)
    Jump("loc_4DA")

    label("loc_4D3")

    OP_6F(0xC, 60)

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC")
    OP_6F(0xD, 0)
    Jump("loc_4F3")

    label("loc_4EC")

    OP_6F(0xD, 60)

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    OP_6F(0xE, 0)
    Jump("loc_50C")

    label("loc_505")

    OP_6F(0xE, 60)

    label("loc_50C")

    Return()

    # Function_1_393 end

    def Function_2_50D(): pass

    label("Function_2_50D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_522")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_50D")

    label("loc_522")

    Return()

    # Function_2_50D end

    def Function_3_523(): pass

    label("Function_3_523")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E0, 1)"), scpexpr(EXPR_END)), "loc_592")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xE0\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1110)
    Jump("loc_5F8")

    label("loc_592")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xE0\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE0\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_5F8")

    Jump("loc_62C")

    label("loc_5FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_62C")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_684")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_684")

    label("loc_64B")


    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xE0\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x1F\xE0\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_684")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_523 end

    def Function_4_68D(): pass

    label("Function_4_68D")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１０\x01",
            "\x07\x02#57I水之耀晶片×１０\x01",
            "\x07\x02#58I火之耀晶片×１０\x01",
            "\x07\x02#59I风之耀晶片×１０\x01",
            "\x07\x02#62I时之耀晶片×１０\x01",
            "\x07\x02#60I空之耀晶片×１０\x01",
            "\x07\x02#61I幻之耀晶片×１０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1111)
    Jump("loc_7C0")

    label("loc_7A6")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_7C0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_68D end

    def Function_5_7D2(): pass

    label("Function_5_7D2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_841")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1112)
    Jump("loc_8A7")

    label("loc_841")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_8A7")

    Jump("loc_8DB")

    label("loc_8AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8DB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7D2 end

    def Function_6_8E9(): pass

    label("Function_6_8E9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_958")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1113)
    Jump("loc_9BE")

    label("loc_958")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_9BE")

    Jump("loc_9F2")

    label("loc_9C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8E9 end

    def Function_7_A00(): pass

    label("Function_7_A00")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25E, 1)"), scpexpr(EXPR_END)), "loc_A6F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\x5E\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1114)
    Jump("loc_AD5")

    label("loc_A6F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\x5E\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5E\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_AD5")

    Jump("loc_B09")

    label("loc_AD8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B09")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A00 end

    def Function_8_B17(): pass

    label("Function_8_B17")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12D, 1)"), scpexpr(EXPR_END)), "loc_B86")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x2D\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1115)
    Jump("loc_BEC")

    label("loc_B86")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x2D\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x2D\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_BEC")

    Jump("loc_C20")

    label("loc_BEF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C20")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B17 end

    def Function_9_C2E(): pass

    label("Function_9_C2E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0D")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_C80():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C80)

    def lambda_C9B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C9B)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #19
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_CE8"),
        (2, "loc_CFA"),
        (1, "loc_D0A"),
        (SWITCH_DEFAULT, "loc_D0D"),
    )


    label("loc_CE8")

    OP_A2(0x1117)
    OP_6F(0xE, 60)
    Sleep(500)
    Jump("loc_D0D")

    label("loc_CFA")

    OP_6F(0xE, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D0A")

    OP_B4(0x0)
    Return()

    label("loc_D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C6, 1)"), scpexpr(EXPR_END)), "loc_D5C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xC6\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1116)
    Jump("loc_DBE")

    label("loc_D5C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xC6\x02\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xC6\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_DBE")

    Jump("loc_DF0")

    label("loc_DC1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DF0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C2E end

    def Function_10_DFE(): pass

    label("Function_10_DFE")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #23
        "有拉杆。是否扳动？\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF7")

    Menu(
        0,
        260,
        200,
        0,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "不动\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA0")
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x10A8)
    OP_6D(3880, 0, 135860, 500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Jump("loc_EED")

    label("loc_EA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EED")
    OP_6F(0x6, 100)
    OP_70(0x6, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x10A7)
    OP_6D(3880, 0, 135860, 500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)

    label("loc_EED")

    OP_69(0x0, 0x258)
    Jump("loc_F94")

    label("loc_EF7")


    Menu(
        0,
        260,
        200,
        0,
        (
            "恢复原状\x01",      # 0
            "不动\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_END)), "loc_F46")
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A3(0x10A8)
    Jump("loc_F66")

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_END)), "loc_F66")
    OP_6F(0x6, 160)
    OP_70(0x6, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A3(0x10A7)

    label("loc_F66")

    OP_6D(3880, 0, 135860, 500)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    OP_69(0x0, 0x258)

    label("loc_F94")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_10_DFE end

    def Function_11_F9D(): pass

    label("Function_11_F9D")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #24
        "有拉杆。是否扳动？\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1096")

    Menu(
        0,
        260,
        200,
        0,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "不动\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103F")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10AA)
    OP_6D(-12270, 0, 174500, 500)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Jump("loc_108C")

    label("loc_103F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108C")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10A9)
    OP_6D(-12270, 0, 174500, 500)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)

    label("loc_108C")

    OP_69(0x0, 0x258)
    Jump("loc_1133")

    label("loc_1096")


    Menu(
        0,
        260,
        200,
        0,
        (
            "恢复原状\x01",      # 0
            "不动\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_END)), "loc_10E5")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10AA)
    Jump("loc_1105")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_END)), "loc_1105")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10A9)

    label("loc_1105")

    OP_6D(-12270, 0, 174500, 500)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    OP_69(0x0, 0x258)

    label("loc_1133")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_11_F9D end

    def Function_12_113C(): pass

    label("Function_12_113C")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #25
        "有拉杆。是否扳动？\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1235")

    Menu(
        0,
        260,
        200,
        0,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "不动\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DE")
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x10AC)
    OP_6D(-8090, -60, 183030, 500)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)
    Jump("loc_122B")

    label("loc_11DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    OP_6F(0x5, 100)
    OP_22(0xFA, 0x0, 0x64)
    OP_70(0x5, 0xA0)
    OP_73(0x5)
    OP_A2(0x10AB)
    OP_6D(-8090, -60, 183030, 500)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)

    label("loc_122B")

    OP_69(0x0, 0x258)
    Jump("loc_12D2")

    label("loc_1235")


    Menu(
        0,
        260,
        200,
        0,
        (
            "恢复原状\x01",      # 0
            "不动\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_END)), "loc_1284")
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x10AC)
    Jump("loc_12A4")

    label("loc_1284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_END)), "loc_12A4")
    OP_6F(0x5, 160)
    OP_70(0x5, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x10AB)

    label("loc_12A4")

    OP_6D(-8090, -60, 183030, 500)
    OP_6F(0x4, 120)
    OP_70(0x4, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)
    OP_69(0x0, 0x258)

    label("loc_12D2")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_12_113C end

    def Function_13_12DB(): pass

    label("Function_13_12DB")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)

    AnonymousTalk(    #26
        "有扳手。是否扳动？\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1366")

    Menu(
        0,
        260,
        200,
        0,
        (
            "降下\x01",      # 0
            "不动\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1363")
    EventBegin(0x0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x7)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xFA)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x0)
    OP_A2(0x10AD)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_1363")

    Jump("loc_13C7")

    label("loc_1366")


    Menu(
        0,
        260,
        200,
        0,
        (
            "拉起\x01",      # 0
            "不动\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")
    EventBegin(0x0)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x7)
    OP_6F(0x0, 250)
    OP_70(0x0, 0x0)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x0)
    OP_A3(0x10AD)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_13C7")

    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_13_12DB end

    SaveToFile()

Try(main)
