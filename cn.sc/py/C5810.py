from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5810   ._SN',
        MapName             = 'Other',
        Location            = 'C5810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '福音',                                 # 9
        '多伦',                                 # 10
        '吉尔',                                 # 11
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
        'ED6_DT26/CH20425 ._CH',             # 00
        'ED6_DT06/CH20021 ._CH',             # 01
        'ED6_DT29/CH12060 ._CH',             # 02
        'ED6_DT29/CH12061 ._CH',             # 03
        'ED6_DT29/CH12190 ._CH',             # 04
        'ED6_DT29/CH12191 ._CH',             # 05
        'ED6_DT29/CH12970 ._CH',             # 06
        'ED6_DT29/CH12971 ._CH',             # 07
        'ED6_DT07/CH02110 ._CH',             # 08
        'ED6_DT07/CH02120 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT26/CH20425P._CP',             # 00
        'ED6_DT06/CH20021P._CP',             # 01
        'ED6_DT29/CH12060P._CP',             # 02
        'ED6_DT29/CH12061P._CP',             # 03
        'ED6_DT29/CH12190P._CP',             # 04
        'ED6_DT29/CH12191P._CP',             # 05
        'ED6_DT29/CH12970P._CP',             # 06
        'ED6_DT29/CH12971P._CP',             # 07
        'ED6_DT07/CH02110P._CP',             # 08
        'ED6_DT07/CH02120P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        ChipIndex           = 0x8,
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
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 500,
        TriggerY            = -67080,
        TriggerRange        = 1500,
        ActorX              = -2810,
        ActorZ              = 1500,
        ActorY              = -67700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 500,
        TriggerY            = -67080,
        TriggerRange        = 1500,
        ActorX              = -2810,
        ActorZ              = 1500,
        ActorY              = -67700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5970,
        TriggerZ            = 0,
        TriggerY            = 11030,
        TriggerRange        = 1500,
        ActorX              = -5970,
        ActorZ              = 1000,
        ActorY              = 11030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 67040,
        TriggerZ            = 0,
        TriggerY            = 9980,
        TriggerRange        = 1500,
        ActorX              = 67040,
        ActorZ              = 1000,
        ActorY              = 9980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 120000,
        TriggerZ            = 0,
        TriggerY            = -1980,
        TriggerRange        = 1500,
        ActorX              = 120000,
        ActorZ              = 1000,
        ActorY              = -1980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8600,
        TriggerZ            = 0,
        TriggerY            = 4940,
        TriggerRange        = 1000,
        ActorX              = 9260,
        ActorZ              = 0,
        ActorY              = 4980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8620,
        TriggerZ            = 0,
        TriggerY            = 1030,
        TriggerRange        = 1000,
        ActorX              = 9240,
        ActorZ              = 0,
        ActorY              = 980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54100,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1000,
        ActorX              = 54100,
        ActorZ              = 0,
        ActorY              = 9710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 120470,
        TriggerZ            = 0,
        TriggerY            = 2140,
        TriggerRange        = 1000,
        ActorX              = 119850,
        ActorZ              = 0,
        ActorY              = 2140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18540,
        TriggerZ            = 0,
        TriggerY            = -75000,
        TriggerRange        = 1000,
        ActorX              = -19160,
        ActorZ              = 0,
        ActorY              = -75000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11080,
        TriggerZ            = 0,
        TriggerY            = -69510,
        TriggerRange        = 1000,
        ActorX              = -11080,
        ActorZ              = 0,
        ActorY              = -68940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18390,
        TriggerZ            = 0,
        TriggerY            = -85010,
        TriggerRange        = 1500,
        ActorX              = -18390,
        ActorZ              = 1000,
        ActorY              = -85010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_3E2",          # 02, 2
        "Function_3_4F9",          # 03, 3
        "Function_4_5D8",          # 04, 4
        "Function_5_6D4",          # 05, 5
        "Function_6_7EB",          # 06, 6
        "Function_7_902",          # 07, 7
        "Function_8_A19",          # 08, 8
        "Function_9_247B",         # 09, 9
        "Function_10_2B4E",        # 0A, 10
        "Function_11_2BD5",        # 0B, 11
        "Function_12_2C68",        # 0C, 12
        "Function_13_30B3",        # 0D, 13
        "Function_14_3516",        # 0E, 14
        "Function_15_35B1",        # 0F, 15
        "Function_16_3AC3",        # 10, 16
        "Function_17_5124",        # 11, 17
        "Function_18_5CCF",        # 12, 18
        "Function_19_5D28",        # 13, 19
        "Function_20_5D81",        # 14, 20
        "Function_21_5E08",        # 15, 21
        "Function_22_5E99",        # 16, 22
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Return()

    # Function_0_30A end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")
    OP_6F(0x0, 0)
    Jump("loc_324")

    label("loc_31D")

    OP_6F(0x0, 60)

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336")
    OP_6F(0x1, 0)
    Jump("loc_33D")

    label("loc_336")

    OP_6F(0x1, 60)

    label("loc_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F")
    OP_6F(0x2, 0)
    Jump("loc_356")

    label("loc_34F")

    OP_6F(0x2, 60)

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    OP_6F(0x3, 0)
    Jump("loc_36F")

    label("loc_368")

    OP_6F(0x3, 60)

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")
    OP_6F(0x4, 0)
    Jump("loc_388")

    label("loc_381")

    OP_6F(0x4, 60)

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A")
    OP_6F(0x5, 0)
    Jump("loc_3A1")

    label("loc_39A")

    OP_6F(0x5, 60)

    label("loc_3A1")

    OP_64(0x7, 0x1)
    OP_71(0x2, 0x0)
    OP_71(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE")
    OP_64(0x1, 0x1)
    Jump("loc_3C2")

    label("loc_3BE")

    OP_64(0x0, 0x1)

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3D3")
    OP_A3(0x10F0)
    Event(0, 16)
    Jump("loc_3E1")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3E1")
    OP_A3(0x10F1)
    Event(0, 17)

    label("loc_3E1")

    Return()

    # Function_1_30B end

    def Function_2_3E2(): pass

    label("Function_2_3E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_451")
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
    OP_A2(0x230D)
    Jump("loc_4B7")

    label("loc_451")

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

    label("loc_4B7")

    Jump("loc_4EB")

    label("loc_4BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3E2 end

    def Function_3_4F9(): pass

    label("Function_3_4F9")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x1, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x5, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00得到了\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230E)
    Jump("loc_5C6")

    label("loc_5AC")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5C6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4F9 end

    def Function_4_5D8(): pass

    label("Function_4_5D8")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x230F)
    Jump("loc_6C2")

    label("loc_6A8")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6C2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5D8 end

    def Function_5_6D4(): pass

    label("Function_5_6D4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_743")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2310)
    Jump("loc_7A9")

    label("loc_743")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_7A9")

    Jump("loc_7DD")

    label("loc_7AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6D4 end

    def Function_6_7EB(): pass

    label("Function_6_7EB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2CC, 1)"), scpexpr(EXPR_END)), "loc_85A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xCC\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2311)
    Jump("loc_8C0")

    label("loc_85A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\xCC\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xCC\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_8C0")

    Jump("loc_8F4")

    label("loc_8C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7EB end

    def Function_7_902(): pass

    label("Function_7_902")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_971")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2312)
    Jump("loc_9D7")

    label("loc_971")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_9D7")

    Jump("loc_A0B")

    label("loc_9DA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A0B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_902 end

    def Function_8_A19(): pass

    label("Function_8_A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3C")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_A3C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05#1S第３５克雷德尔·市政厅窗口\x01\x01",
            "※除了登记在册的利贝尔·方舟市民之外，\x01",
            "  无法利用各项服务。\x01\x01",
            "※现在，由于和『中枢塔』之间的通讯\x01",
            "  发生异常，因此可以利用的服务种类\x01",
            "  受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2446")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x0)
    OP_CC(0x1, 0x0, "【使用数据库】")
    OP_CC(0x1, 0x0, "【福音的再发行申请】")
    OP_CC(0x1, 0x0, "【放弃使用】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B94"),
        (1, "loc_10C5"),
        (2, "loc_2424"),
        (SWITCH_DEFAULT, "loc_2443"),
    )


    label("loc_B94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #17
        (
            "\x07\x05#1S现在可以参阅的项目受到了一定的限制。\x01",
            "丂\x01",
            "请选择项目。\x02",
        )
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x1, 0x28, 0xBE, 0x1)
    OP_CC(0x1, 0x1, "【光环轨道】")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C1C"),
        (SWITCH_DEFAULT, "loc_10A5"),
    )


    label("loc_C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1095")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x2, 0x28, 0xFA, 0x1)
    OP_CC(0x1, 0x2, "【关于光环轨道】")
    OP_CC(0x1, 0x2, "【关于各站的终端】")
    OP_CC(0x1, 0x2, "【关于紧急运行模式】")
    OP_CC(0x2, 0x2)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CA1"),
        (1, "loc_E2D"),
        (2, "loc_F5D"),
        (SWITCH_DEFAULT, "loc_1085"),
    )


    label("loc_CA1")


    AnonymousTalk(    #18
        (
            "\x07\x05#1S『光环轨道』是一种独一无二，\x01",
            "本都市特有的跨时代移动手段。\x01\x01",
            "#1S在本都市建立起的空间干涉技术，\x01",
            "让借由特殊力场对空间展开轨道成为了可能，\x01",
            "传统的实体轨道因此走向废除的命运。\x01\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #19
        (
            "\x07\x05#1S这种特殊力场最大的特点，\x01",
            "就是它的发生场所完全不受限制。\x01",
            "也就是说，它可以让散布在都市各处\x01",
            "的无数车站灵活地直接连结在一起。\x01\x01",
            "#1S『光环轨道』保障了市民们\x01",
            "便利而舒适的都市生活。\x01",
            "当您有事要到其它地区时请多利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_E2D")


    AnonymousTalk(    #20
        (
            "\x07\x05#1S各地区『光环轨道』的终端\x01",
            "#1S除发售车票之外，\x01",
            "还受理其它各项服务。\x01\x01",
            "#1S在其中的【网络商店】里，\x01",
            "市民可以进行日用品的采购，\x01",
            "同时也贩卖各种票券等等，\x01",
            "欢迎多加利用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #21
        (
            "\x07\x05#1S此外，当『光环轨道』\x01",
            "由于各种原因而无法使用时，\x01",
            "可以利用车站终端来启动\x01",
            "紧急运行模式，或是解除\x01",
            "通往车站周边的地下通路锁定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_F5D")


    AnonymousTalk(    #22
        (
            "\x07\x05#1S紧急运行模式正如其名，\x01",
            "是指紧急时的启动的模式。\x01\x01",
            "#1S当某些原因导致来自『中枢塔』\x01",
            "的能量供给陷入困难的情况下时，\x01",
            "可借由启动这个模式\x01",
            "来切换到备用能量。\x01",
            "如此一来便可让『光环轨道』\x01",
            "暂时能够运行。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #23
        (
            "\x07\x05#1S此外，由于该模式\x01",
            "是由各车站所个别控制，\x01",
            "因此无法移动至尚未启动\x01",
            "紧急运行模式的车站。\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_1085")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1092")

    label("loc_1092")

    Jump("loc_C1C")

    label("loc_1095")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B2")

    label("loc_10A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B2")

    label("loc_10B2")

    Jump("loc_B94")

    label("loc_10B5")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2443")

    label("loc_10C5")

    OP_A2(0x22D1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05#1S现在由于和『中枢塔』之间\x01",
            "的通讯发生异常，因此\x01",
            "再发行的福音纯属临时性质。\x01\x01",
            "为了与本终端的数据库进行核对，\x01",
            "请输入申请者本人的姓名。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x3C, 0xAA, 0x9, "#2C输入谁的姓名呢？")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x1, 0x55, 0x104, 0x0)
    OP_CC(0x1, 0x1, "【艾丝蒂尔】")
    OP_CC(0x1, 0x1, "【约修亚】")
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_11EE"),
        (3, "loc_1201"),
        (4, "loc_1214"),
        (5, "loc_1225"),
        (6, "loc_1236"),
        (7, "loc_1245"),
        (8, "loc_1252"),
        (10, "loc_1261"),
        (SWITCH_DEFAULT, "loc_1272"),
    )


    label("loc_11EE")

    OP_CC(0x1, 0x1, "【雪拉扎德】")
    Jump("loc_1272")

    label("loc_1201")

    OP_CC(0x1, 0x1, "【奥利维尔】")
    Jump("loc_1272")

    label("loc_1214")

    OP_CC(0x1, 0x1, "【科洛丝】")
    Jump("loc_1272")

    label("loc_1225")

    OP_CC(0x1, 0x1, "【阿加特】")
    Jump("loc_1272")

    label("loc_1236")

    OP_CC(0x1, 0x1, "【提妲】")
    Jump("loc_1272")

    label("loc_1245")

    OP_CC(0x1, 0x1, "【金】")
    Jump("loc_1272")

    label("loc_1252")

    OP_CC(0x1, 0x1, "【凯文】")
    Jump("loc_1272")

    label("loc_1261")

    OP_CC(0x1, 0x1, "【乔丝特】")
    Jump("loc_1272")

    label("loc_1272")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_129B"),
        (3, "loc_12AE"),
        (4, "loc_12C1"),
        (5, "loc_12D2"),
        (6, "loc_12E3"),
        (7, "loc_12F2"),
        (8, "loc_12FF"),
        (10, "loc_130E"),
        (SWITCH_DEFAULT, "loc_131F"),
    )


    label("loc_129B")

    OP_CC(0x1, 0x1, "【雪拉扎德】")
    Jump("loc_131F")

    label("loc_12AE")

    OP_CC(0x1, 0x1, "【奥利维尔】")
    Jump("loc_131F")

    label("loc_12C1")

    OP_CC(0x1, 0x1, "【科洛丝】")
    Jump("loc_131F")

    label("loc_12D2")

    OP_CC(0x1, 0x1, "【阿加特】")
    Jump("loc_131F")

    label("loc_12E3")

    OP_CC(0x1, 0x1, "【提妲】")
    Jump("loc_131F")

    label("loc_12F2")

    OP_CC(0x1, 0x1, "【金】")
    Jump("loc_131F")

    label("loc_12FF")

    OP_CC(0x1, 0x1, "【凯文】")
    Jump("loc_131F")

    label("loc_130E")

    OP_CC(0x1, 0x1, "【乔丝特】")
    Jump("loc_131F")

    label("loc_131F")

    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_133E"),
        (1, "loc_134B"),
        (2, "loc_1358"),
        (3, "loc_137C"),
        (SWITCH_DEFAULT, "loc_13A0"),
    )


    label("loc_133E")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A0")

    label("loc_134B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A0")

    label("loc_1358")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1379")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1379")

    Jump("loc_13A0")

    label("loc_137C")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139D")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_139D")

    Jump("loc_13A0")

    label("loc_13A0")

    OP_5F(0x1)
    OP_5F(0x2)
    OP_57(0x28, 0xAA, 0xB, "#2C请输入姓名。")

    Menu(
        1,
        70,
        260,
        0,
        (
            "【乌路里希】\x01",        # 0
            "【盖鲁格】\x01",          # 1
            "【亚奥伊斯】\x01",        # 2
            "【赛雷斯托】\x01",        # 3
            "【爱德路霍富】\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1421")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1421")

    OP_5F(0x1)

    Menu(
        1,
        110,
        260,
        0,
        (
            "【Ａ】\x01",      # 0
            "【Ｂ】\x01",      # 1
            "【Ｃ】\x01",      # 2
            "【Ｄ】\x01",      # 3
            "【Ｅ】\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146A")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_146A")

    OP_5F(0x1)

    Menu(
        1,
        65,
        260,
        0,
        (
            "【阿斯特雷】\x01",        # 0
            "【怀斯曼】\x01",          # 1
            "【爱普斯泰恩】\x01",      # 2
            "【奥赛雷丝】\x01",        # 3
            "【莱恩福尔特】\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14D3")

    OP_5F(0x1)
    OP_DA()
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    EventBegin(0x0)
    OP_D2(0x60065, 0x6006A, 0x1)
    OP_6D(-3670, 230, -66890, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_1566"),
        (1, "loc_15AD"),
        (2, "loc_15F4"),
        (3, "loc_163B"),
        (SWITCH_DEFAULT, "loc_1682"),
    )


    label("loc_1566")

    SetChrPos(0x101, -2790, 500, -68180, 0)
    SetChrPos(0x102, -2680, 220, -69410, 0)
    SetChrPos(0xF8, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_1682")

    label("loc_15AD")

    SetChrPos(0x102, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0xF8, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_1682")

    label("loc_15F4")

    SetChrPos(0xF8, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0x102, -1230, 0, -69950, 315)
    SetChrPos(0xF9, -3450, 220, -69930, 0)
    Jump("loc_1682")

    label("loc_163B")

    SetChrPos(0xF9, -2790, 500, -68180, 0)
    SetChrPos(0x101, -2680, 220, -69410, 0)
    SetChrPos(0x102, -1230, 0, -69950, 315)
    SetChrPos(0xF8, -3450, 220, -69930, 0)
    Jump("loc_1682")

    label("loc_1682")

    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C10")
    SetChrName("合成音")

    AnonymousTalk(    #25
        (
            "\x07\x05姓名………………………赛雷斯托·Ｄ·奥赛雷丝\x01",
            "基因验证…………………７３％吻合\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #26
        (
            "\x07\x05暂时认定\x01",
            "申请者为\x01",
            "【赛雷斯托·Ｄ·奥赛雷丝】\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #27
        "\x07\x05现在进行『福音』的再发行。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    LoadEffect(0x0, "map\\\\mp027_01.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, -2810, 2500, -67130, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_22(0x99, 0x0, 0x64)

    def lambda_17C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17C7)
    OP_91(0x8, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x2)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        "#1164F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1004F哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1042F是空间转换吗……\x02",
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x8, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x1F\x0F\x04\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x40F, 1)
    OP_8C(0x105, 180, 400)

    ChrTalk(    #32
        0x105,
        (
            "#1160F#2P……好像是远古时代\x01",
            "曾经使用过的真正『福音』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1002F嗯……感觉和『结社』\x01",
            "制造的复制品很相似。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1040F果然，在四轮之塔终端的\x01",
            "那位『赛雷斯托·Ｄ·奥赛雷丝』\x01",
            "似乎就是科洛丝的祖先呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#1160F#2P是的……\x02\x03",

            "#1167F或许就是让市民们\x01",
            "从这座都市里逃出的负责人吧。\x02\x03",

            "#1382F至于基因验证和我相似，\x01",
            "我想大概是偶然凑巧吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在车站终端查阅『福音』的信息】\x01",          # 0
            "【◇不在车站的终端查阅『福音』的信息】\x01",      # 1
            "【◇什么也没有变更】\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A8F"),
        (1, "loc_1A95"),
        (SWITCH_DEFAULT, "loc_1A9B"),
    )


    label("loc_1A8F")

    OP_A2(0x221A)
    Jump("loc_1A9B")

    label("loc_1A95")

    OP_A3(0x221A)
    Jump("loc_1A9B")

    label("loc_1A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 2)), scpexpr(EXPR_END)), "loc_1B55")

    ChrTalk(    #36
        0x101,
        (
            "#1001F嘿嘿，也许不是偶然，\x01",
            "而是女神的指引呢。\x02\x03",

            "#1006F总之，在车站的终端使用这个，\x01",
            "似乎就可以打开通往地下的大门了。\x02\x03",

            "我们马上去试试吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #37
        0x105,
        "#1161F#2P嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BEF")

    label("loc_1B55")


    ChrTalk(    #38
        0x101,
        (
            "#1001F嘿嘿，也许不是偶然，\x01",
            "而是女神的指引呢。\x02\x03",

            "#1006F总之，带着它\x01",
            "说不定会有什么帮助……\x02\x03",

            "就心怀感激地收下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #39
        0x105,
        "#1168F#2P呵呵，说得也是。\x02",
    )

    CloseMessageWindow()

    label("loc_1BEF")

    OP_A2(0x221B)
    OP_64(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_28(0x9D, 0x1, 0x800)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2443")

    label("loc_1C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF1")
    SetChrName("合成音")

    AnonymousTalk(    #40
        (
            "\x07\x05姓名………………………无此者\x01",
            "基因验证…………………无此者\x01",
            "请输入正确的姓名。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDE")

    ChrTalk(    #41
        0x101,
        "#1004F怎、怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1035F看来会将当时的市民姓名\x01",
            "与基因验证彼此进行相互核对。\x02\x03",

            "#1040F但是，基因验证吻合\x01",
            "也就是说……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    ChrTalk(    #43
        0x105,
        (
            "#1167F#2P是的，或许是我的基因验证\x01",
            "与哪位祖先相似也说不定。\x02\x03",

            "#1162F接下来只要知道姓名的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1002F科洛丝的祖先姓名吗……\x02\x03",

            "#1015F（咦……？\x01",
            "好像有点印象……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_1E55")

    ChrTalk(    #45
        0x102,
        (
            "#1040F无论如何，正像博士所说的，\x01",
            "看来我们需要了解一下过去的事情了。\x02\x03",

            "我们暂时先返回埃尔赛尤号，\x01",
            "看看『卡佩尔』从数据水晶解读出来的信息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC1")

    label("loc_1E55")


    ChrTalk(    #46
        0x102,
        (
            "#1040F不管怎么说，\x01",
            "这似乎是个相当精密的系统。\x02\x03",

            "还是暂时先返回埃尔赛尤号，\x01",
            "与拉赛尔博士商量一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC1")

    OP_8C(0x105, 0, 400)
    OP_A2(0x0)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05\x02",
    )

    Jump("loc_2443")

    label("loc_1EDE")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05\x02",
    )

    Jump("loc_2421")

    label("loc_1EF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B4")
    SetChrName("合成音")

    AnonymousTalk(    #49
        (
            "\x07\x05姓名………………………赛雷斯托·Ｄ·奥赛雷丝\x01",
            "基因验证…………………不一致\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #50
        "\x07\x05中断再发行手续。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A1")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_1F9B"),
        (1, "loc_1F9E"),
        (2, "loc_1FA1"),
        (3, "loc_1FA4"),
        (SWITCH_DEFAULT, "loc_1FA7"),
    )


    label("loc_1F9B")

    Jump("loc_1FA7")

    label("loc_1F9E")

    Jump("loc_1FA7")

    label("loc_1FA1")

    Jump("loc_1FA7")

    label("loc_1FA4")

    Jump("loc_1FA7")

    label("loc_1FA7")


    ChrTalk(    #51
        0x101,
        "#1004F怎、怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035F看来会将当时的市民姓名\x01",
            "与基因验证彼此进行相互核对。\x02\x03",

            "#1043F虽然有符合的姓名，\x01",
            "但基因验证不吻合……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F嗯……\x01",
            "看来真的一点办法也没有了。\x02\x03",

            "#1015F（咦……？\x01",
            "不过说到奥赛雷丝……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_211F")

    ChrTalk(    #54
        0x102,
        (
            "#1040F无论如何，正像博士所说的，\x01",
            "看来我们需要了解一下过去的事情了。\x02\x03",

            "我们暂时先返回埃尔赛尤号，\x01",
            "看看『卡佩尔』从数据水晶解读出来的信息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218B")

    label("loc_211F")


    ChrTalk(    #55
        0x102,
        (
            "#1040F不管怎么说，\x01",
            "这似乎是个相当精密的系统。\x02\x03",

            "还是暂时先返回埃尔赛尤号，\x01",
            "与拉赛尔博士商量一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218B")

    OP_A2(0x1)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05\x02",
    )

    Jump("loc_2443")

    label("loc_21A1")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05\x02",
    )

    Jump("loc_2421")

    label("loc_21B4")

    SetChrName("合成音")

    AnonymousTalk(    #58
        (
            "\x07\x05姓名………………………无此者\x01",
            "基因验证…………………无此者\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #59
        "\x07\x05中断再发行手续。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2411")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_2236"),
        (1, "loc_2239"),
        (2, "loc_223C"),
        (3, "loc_223F"),
        (SWITCH_DEFAULT, "loc_2242"),
    )


    label("loc_2236")

    Jump("loc_2242")

    label("loc_2239")

    Jump("loc_2242")

    label("loc_223C")

    Jump("loc_2242")

    label("loc_223F")

    Jump("loc_2242")

    label("loc_2242")


    ChrTalk(    #60
        0x101,
        "#1004F怎、怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1035F看来会将当时的市民姓名\x01",
            "与基因验证彼此进行相互核对。\x02\x03",

            "#1042F如果二者不能吻合，\x01",
            "就无法继续办理手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1019F嗯……\x01",
            "老实说，有束手无策的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_END)), "loc_2391")

    ChrTalk(    #63
        0x102,
        (
            "#1040F无论如何，正像博士所说的，\x01",
            "看来我们需要了解一下过去的事情了。\x02\x03",

            "我们暂时先返回埃尔赛尤号，\x01",
            "看看『卡佩尔』从数据水晶解读出来的信息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23FB")

    label("loc_2391")


    ChrTalk(    #64
        0x102,
        (
            "#1040F不管怎么说\x01",
            "这似乎是个相当精密的系统。\x02\x03",

            "还是暂时先返回埃尔赛尤号，\x01",
            "与拉赛尔博士商量一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FB")

    OP_A2(0x2)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x05\x02",
    )

    Jump("loc_2443")

    label("loc_2411")

    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05\x02",
    )


    label("loc_2421")

    Jump("loc_2443")

    label("loc_2424")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2443")

    label("loc_2443")

    Jump("loc_B17")

    label("loc_2446")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2474")
    EventEnd(0x0)

    label("loc_2474")

    OP_A3(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A19 end

    def Function_9_247B(): pass

    label("Function_9_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_249E")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_249E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #67
        (
            "\x07\x05#1S第３５克雷德尔·市政厅窗口\x01\x01",
            "※除了登记在册的利贝尔·方舟市民之外，\x01",
            "  无法利用各种服务。\x01\x01",
            "※现在，由于和『中枢塔』之间的通讯\x01",
            "  发生异常，因此可以利用的服务种类\x01",
            "  受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2577")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B25")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x64, 0x0)
    OP_CC(0x1, 0x0, "【使用数据库】")
    OP_CC(0x1, 0x0, "【放弃使用】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25D2"),
        (0, "loc_25D2"),
        (1, "loc_2B03"),
        (SWITCH_DEFAULT, "loc_2B22"),
    )


    label("loc_25D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #68
        (
            "\x07\x05#1S现在可以参阅的项目受到了一定的限制。\x01",
            "丂\x01",
            "请选择项目。\x02",
        )
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x1, 0x28, 0xB4, 0x1)
    OP_CC(0x1, 0x1, "【光环轨道】")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_265A"),
        (SWITCH_DEFAULT, "loc_2AE3"),
    )


    label("loc_265A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AD3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x2, 0x28, 0xF0, 0x1)
    OP_CC(0x1, 0x2, "【关于光环轨道】")
    OP_CC(0x1, 0x2, "【关于各站的终端】")
    OP_CC(0x1, 0x2, "【关于紧急运行模式】")
    OP_CC(0x2, 0x2)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26DF"),
        (1, "loc_286B"),
        (2, "loc_299B"),
        (SWITCH_DEFAULT, "loc_2AC3"),
    )


    label("loc_26DF")


    AnonymousTalk(    #69
        (
            "\x07\x05#1S『光环轨道』是一种独一无二，\x01",
            "本都市特有的跨时代移动手段。\x01\x01",
            "#1S在本都市建立起的空间干涉技术，\x01",
            "让借由特殊力场对空间展开轨道成为了可能，\x01",
            "传统的实体轨道因此走向废除的命运。\x01\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x07\x05#1S这种特殊力场最大的特点，\x01",
            "就是它的发生场所完全不受限制。\x01",
            "也就是说，它可以让散布在都市各处\x01",
            "的无数车站灵活地直接连结在一起。\x01\x01",
            "#1S『光环轨道』保障了市民们\x01",
            "便利而舒适的都市生活。\x01",
            "当您有事要到其它地区时请多利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD0")

    label("loc_286B")


    AnonymousTalk(    #71
        (
            "\x07\x05#1S各地区『光环轨道』的终端\x01",
            "#1S除发售车票之外，\x01",
            "还受理其它各项服务。\x01\x01",
            "#1S在其中的【网络商店】里，\x01",
            "市民可以进行日用品的采购，\x01",
            "同时也贩卖各种票券等等，\x01",
            "欢迎多加利用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        (
            "\x07\x05#1S此外，当『光环轨道』\x01",
            "由于各种原因而无法使用时，\x01",
            "可以利用车站终端来启动\x01",
            "紧急运行模式，或是解除\x01",
            "通往车站周边的地下通路锁定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD0")

    label("loc_299B")


    AnonymousTalk(    #73
        (
            "\x07\x05#1S紧急运行模式正如其名，\x01",
            "是指紧急时的启动的模式。\x01\x01",
            "#1S当某些原因导致来自『中枢塔』\x01",
            "的能量供给陷入困难的情况下时，\x01",
            "可借由启动这个模式\x01",
            "来切换到备用能量。\x01",
            "如此一来便可让『光环轨道』\x01",
            "暂时能够运行。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        (
            "\x07\x05#1S此外，由于该模式\x01",
            "是由各车站所个别控制，\x01",
            "因此无法移动至尚未启动\x01",
            "紧急运行模式的车站。\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD0")

    label("loc_2AC3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AD0")

    label("loc_2AD0")

    Jump("loc_265A")

    label("loc_2AD3")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AF0")

    label("loc_2AE3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AF0")

    label("loc_2AF0")

    Jump("loc_25D2")

    label("loc_2AF3")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B22")

    label("loc_2B03")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B22")

    label("loc_2B22")

    Jump("loc_2577")

    label("loc_2B25")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_9_247B end

    def Function_10_2B4E(): pass

    label("Function_10_2B4E")

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
        (0, "loc_2BC8"),
        (1, "loc_2BCE"),
        (SWITCH_DEFAULT, "loc_2BD4"),
    )


    label("loc_2BC8")

    OP_A2(0x1200)
    Jump("loc_2BD4")

    label("loc_2BCE")

    OP_A2(0x1201)
    Jump("loc_2BD4")

    label("loc_2BD4")

    Return()

    # Function_10_2B4E end

    def Function_11_2BD5(): pass

    label("Function_11_2BD5")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_2BD5 end

    def Function_12_2C68(): pass

    label("Function_12_2C68")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #75
        (
            "\x07\x05#1S第３５克雷德尔·居住者用终端\x01",
            "　　　　　　　　　　　＃C035-556800015073\x01",
            "丂\x01",
            "#1SＩＤ确认中#100W……………………………#20W不符合。\x01",
            "丂\x01",
            "※无法确认终端所有者的ＩＤ。\x01",
            "　允许阅览的项目受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x0)
    OP_CC(0x1, 0x0, "【确认新食谱】")
    OP_CC(0x1, 0x0, "【放弃使用】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DB9"),
        (1, "loc_3068"),
        (SWITCH_DEFAULT, "loc_3087"),
    )


    label("loc_2DB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3058")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #76
        (
            "\x07\x05#1S===============料理＃W-6894===============\x01",
            "==============大麦奶酪果冻==============\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x32, 0x9B, 0x9, "#2C要转录资料吗？")
    OP_CC(0x0, 0x1, 0x28, 0xF0, 0x0)
    OP_CC(0x1, 0x1, "【是】")
    OP_CC(0x1, 0x1, "【否】")
    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E8A"),
        (1, "loc_3047"),
        (SWITCH_DEFAULT, "loc_3047"),
    )


    label("loc_2E8A")

    OP_DA()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3027")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4B)"), scpexpr(EXPR_END)), "loc_2EC4")

    AnonymousTalk(    #77
        "\x07\x05#1S食谱数据已经开始转录。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3024")

    label("loc_2EC4")

    OP_AC(0x4B)

    AnonymousTalk(    #78
        "\x07\x05#1S数据转录中#100W……………………#20W完成！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    FadeToBright(300, 0)
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x1F\xC8\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #80
        0x101,
        (
            "#1004F哇，料理手册上\x01",
            "被写进了新资料！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA7")

    ChrTalk(    #81
        0x102,
        (
            "#065F……究、究竟\x01",
            "是怎么做到的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC8")

    label("loc_2FA7")


    ChrTalk(    #82
        0x102,
        (
            "#1044F……究竟\x01",
            "是什么原理？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC8")


    ChrTalk(    #83
        0x101,
        (
            "#1015F嗯，虽然不太了解，\x01",
            "不过真是了不起的技术啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #84
        "\x07\x05#1S\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3024")

    Jump("loc_3044")

    label("loc_3027")


    AnonymousTalk(    #85
        "\x07\x05#1S找不到数据转录对象。\x02",
    )

    CloseMessageWindow()

    label("loc_3044")

    Jump("loc_3055")

    label("loc_3047")

    OP_DA()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3055")

    label("loc_3055")

    Jump("loc_2DB9")

    label("loc_3058")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3087")

    label("loc_3068")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3087")

    label("loc_3087")

    Jump("loc_2D58")

    label("loc_308A")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_12_2C68 end

    def Function_13_30B3(): pass

    label("Function_13_30B3")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #86
        (
            "\x07\x05#1S第３５克雷德尔·居住者用终端\x01",
            "　　　　　　　　　　　＃C035-556800014096\x01",
            "　\x01",
            "#1SＩＤ确认中#100W……………………………#20W不符合。\x01",
            "丂\x01",
            "※无法确认终端所有者的ＩＤ。\x01",
            "　允许阅览的项目受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34ED")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x0)
    OP_CC(0x1, 0x0, "【留言板】")
    OP_CC(0x1, 0x0, "【放弃使用】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3200"),
        (1, "loc_34CB"),
        (SWITCH_DEFAULT, "loc_34EA"),
    )


    label("loc_3200")


    AnonymousTalk(    #87
        (
            "\x07\x05#1S『关于强化都市警备的通知』\x01",
            "　\x01",
            "近年来，在法克特里亚等\x01",
            "人烟稀少的地区里，\x01",
            "犯罪数目明显增加。\x01",
            "迄今为止，我们竭尽所能地\x01",
            "在确保市民自由的基础上，\x01",
            "不断地进行警备力量的强化。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x05#1S然而，犯罪率\x01",
            "依旧一路向上攀升。\x01",
            "讨论后的结果是，没有市民的配合，\x01",
            "就无法达成万全的警备，\x01",
            "因此希望大家能够提供协助。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05#1S为此，我们衷心希望\x01",
            "各位市民能够理解以下事项。\x01",
            "丂\x01",
            "·在使用终端时，\x01",
            "　将全面进行各位的『福音』ＩＤ认证。\x01",
            "·在『利贝尔·方舟』市的所有地区\x01",
            "　将实施定期性的盘查活动。\x01",
            "·在没有许可的情况下，\x01",
            "　将限制普通住户前往『中枢塔』。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        (
            "\x07\x05#1S这次的警备强化\x01",
            "多少干涉了市民的行动自由，\x01",
            "也许会因此为您带来些许的不愉快。\x01",
            "但这也是优先考虑都市与各位市民安全\x01",
            "所得到的结果。\x01",
            "期望各位的理解与合作。\x01",
            "丂\x01",
            "『利贝尔·方舟』市·警备局\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EA")

    label("loc_34CB")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34EA")

    label("loc_34EA")

    Jump("loc_31A3")

    label("loc_34ED")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_13_30B3 end

    def Function_14_3516(): pass

    label("Function_14_3516")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("合成音")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05欢迎来到克雷德尔·市政厅！\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #92
        "\x07\x05现在为非受理时间。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #93
        (
            "\x07\x05有事请在里面的窗口\x01",
            "选择直接服务。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_3516 end

    def Function_15_35B1(): pass

    label("Function_15_35B1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #94
        (
            "\x07\x05#1S第３５克雷德尔·居住者用终端\x01",
            "　　　　　　　　　　　＃C035-556800014096\x01",
            "丂\x01",
            "#1SＩＤ确认中#100W……………………………#20W不符合。\x01",
            "　\x01",
            "※无法确认终端所有者的ＩＤ。\x01",
            "　允许阅览的项目受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A9A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x28, 0x5A, 0x0)
    OP_CC(0x1, 0x0, "【留言板】")
    OP_CC(0x1, 0x0, "【放弃使用】")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36FE"),
        (1, "loc_3A78"),
        (SWITCH_DEFAULT, "loc_3A97"),
    )


    label("loc_36FE")


    AnonymousTalk(    #95
        (
            "\x07\x05#1S『【重要】关于强化个人播送服务和\x01",
            "　　　　　更新『福音』的通知』\x01",
            "丂\x01",
            "『利贝尔·方舟』市，\x01",
            "为了给市民们营造\x01",
            "舒适而充实的都市生活，\x01",
            "我们实施了以『治愈』为主题\x01",
            "的各种音乐和影像的播送服务。\x01",
            "此一服务除了一般的大众之外，\x01",
            "也受到了因精神疾病而困扰的患者\x01",
            "一致的热烈好评。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #96
        (
            "\x07\x05#1S然而，目前这类服务\x01",
            "尽管有一定的可选择性，\x01",
            "但总体来说是统一且单方面的，\x01",
            "因此近来不断听到要求广泛对应\x01",
            "每一个人兴趣爱好的声音。\x01",
            "丂\x01",
            "我们接受了这种意见，并且为了提供\x01",
            "拥有不同嗜好的所有市民充实的服务，\x01",
            "我们正在加强播送服务方面的多样性\x01",
            "和独创性，同时一步步考虑要如何\x01",
            "提供大家更便捷、更适合的服务。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #97
        (
            "\x07\x05#1S为此，首先必须对全体市民的\x01",
            "『福音』进行更新。\x01",
            "基于上述理由，\x01",
            "请大家前往附近的市政厅询问之后，\x01",
            "同时办理更新手续。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #98
        (
            "\x07\x05#1S此外，本次更新以全体市民为实施对象，\x01",
            "未经更新的『福音』\x01",
            "在经过一段的期间之后\x01",
            "将无法继续使用。\x01",
            "这或许多少会给大家带来一些麻烦，\x01",
            "但衷心期望您能够与我们配合。\x01",
            "丂\x01",
            "『利贝尔·方舟』市·系统管理局\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A97")

    label("loc_3A78")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A97")

    label("loc_3A97")

    Jump("loc_36A1")

    label("loc_3A9A")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_15_35B1 end

    def Function_16_3AC3(): pass

    label("Function_16_3AC3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE8")
    Call(0, 10)
    Call(0, 21)
    AddParty(0x45, 0xFA, 0xFF)

    label("loc_3AE8")

    OP_D2(0x270003, 0x270007, 0xA)
    OP_D2(0x270013, 0x270017, 0xB)
    OP_D2(0x2700A3, 0x2700A7, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_3B2B"),
        (3, "loc_3B38"),
        (4, "loc_3B45"),
        (5, "loc_3B52"),
        (6, "loc_3B5F"),
        (7, "loc_3B6C"),
        (8, "loc_3B79"),
        (SWITCH_DEFAULT, "loc_3B86"),
    )


    label("loc_3B2B")

    OP_D2(0x70023, 0x7002B, 0xD)
    Jump("loc_3B86")

    label("loc_3B38")

    OP_D2(0x70033, 0x7003B, 0xD)
    Jump("loc_3B86")

    label("loc_3B45")

    OP_D2(0x27039B, 0x27039F, 0xD)
    Jump("loc_3B86")

    label("loc_3B52")

    OP_D2(0x70053, 0x7005B, 0xD)
    Jump("loc_3B86")

    label("loc_3B5F")

    OP_D2(0x70063, 0x7006B, 0xD)
    Jump("loc_3B86")

    label("loc_3B6C")

    OP_D2(0x70073, 0x7007B, 0xD)
    Jump("loc_3B86")

    label("loc_3B79")

    OP_D2(0x270083, 0x270087, 0xD)
    Jump("loc_3B86")

    label("loc_3B86")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3BAB"),
        (3, "loc_3BB8"),
        (4, "loc_3BC5"),
        (5, "loc_3BD2"),
        (6, "loc_3BDF"),
        (7, "loc_3BEC"),
        (8, "loc_3BF9"),
        (SWITCH_DEFAULT, "loc_3C06"),
    )


    label("loc_3BAB")

    OP_D2(0x70023, 0x7002B, 0xE)
    Jump("loc_3C06")

    label("loc_3BB8")

    OP_D2(0x70033, 0x7003B, 0xE)
    Jump("loc_3C06")

    label("loc_3BC5")

    OP_D2(0x27039B, 0x27039F, 0xE)
    Jump("loc_3C06")

    label("loc_3BD2")

    OP_D2(0x70053, 0x7005B, 0xE)
    Jump("loc_3C06")

    label("loc_3BDF")

    OP_D2(0x70063, 0x7006B, 0xE)
    Jump("loc_3C06")

    label("loc_3BEC")

    OP_D2(0x70073, 0x7007B, 0xE)
    Jump("loc_3C06")

    label("loc_3BF9")

    OP_D2(0x270083, 0x270087, 0xE)
    Jump("loc_3C06")

    label("loc_3C06")

    OP_6D(59810, 0, -1090, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(4450, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x146, 12)
    SetChrChipByIndex(0xF8, 13)
    SetChrChipByIndex(0xF9, 14)
    SetChrSubChip(0xF9, 1)
    SetChrFlags(0x146, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x146, 59020, 200, 3010, 90)
    SetChrPos(0x101, 60220, 200, 4430, 180)
    SetChrPos(0x102, 60040, 200, 1600, 0)
    SetChrPos(0xF8, 61850, 200, 4460, 180)
    SetChrPos(0xF9, 61850, 200, 1520, 0)

    def lambda_3CD5():
        OP_6D(59860, 0, 4019, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CD5)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #99
        0x146,
        (
            "#413F#5P……对不起……\x01",
            "好像吓到你们了。\x02\x03",

            "#210F我没事，已经平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1019F真是的……\x01",
            "害我吓了一大跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#1035F#6P那么，乔丝特……\x02\x03",

            "#1042F能将其它人被捕时的情况\x01",
            "详细地告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x146, 2)
    Sleep(300)

    ChrTalk(    #102
        0x146,
        (
            "#215F#5P……嗯……\x02\x03",

            "#212F我们坠落到这里之后，\x01",
            "马上就开始着手修理『山猫号』。\x02\x03",

            "虽然引擎平安无事，\x01",
            "可是其它装置全部都损坏了……\x02\x03",

            "所以我们试着在这附近进行探索，\x01",
            "看看有没有可以用来修理的材料……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F0F")

    ChrTalk(    #103
        0x106,
        (
            "#555F嗯……\x01",
            "和我们的情况差不多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4018")

    label("loc_3F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F41")

    ChrTalk(    #104
        0x108,
        "#070F和我们的情况差不多啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4018")

    label("loc_3F41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F7E")

    ChrTalk(    #105
        0x103,
        (
            "#020F原来如此。\x01",
            "和我们的情况差不多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4018")

    label("loc_3F7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB1")

    ChrTalk(    #106
        0x109,
        "#1063F和我们的情况差不多呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4018")

    label("loc_3FB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FEA")

    ChrTalk(    #107
        0x104,
        (
            "#030F嗯……\x01",
            "和我们的情况差不多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4018")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4018")

    ChrTalk(    #108
        0x105,
        "#1162F和我们的情况差不多呢\x02",
    )

    CloseMessageWindow()

    label("loc_4018")


    ChrTalk(    #109
        0x146,
        (
            "#215F#5P……大约三天之后吧……\x02\x03",

            "当我们找齐了原先不足的材料，\x01",
            "正准备进行正式的修复工作时，\x01",
            "像章鱼的那种人形兵器出现了……\x02\x03",

            "#413F当我击中它之后，\x01",
            "红色飞艇就飞了过来……\x02\x03",

            "一着陆，那些猎兵们\x01",
            "就三三两两地跑下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#1043F#6P把正在警戒行动中的\x01",
            "『哨兵』打倒了吗……\x02\x03",

            "#1035F大概是被破坏时所发出的\x01",
            "紧急信号传送到敌人那里了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x146,
        (
            "#216F#5P果然是这样……\x02\x03",

            "#215F怎、怎么办……\x02\x03",

            "都怪我做了多余的事情。\x01",
            "害得大哥他们和大家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#1043F#6P乔丝特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1022F啊～真是的！\x01",
            "别摆出那种表情嘛！\x02\x03",

            "#1005F被抓住的话，\x01",
            "去救出来不就行了吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x146, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x146, 0)

    ChrTalk(    #114
        0x146,
        "#213F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1006F即使是罪犯，\x01",
            "只要遭到了不当监禁，\x01",
            "就是游击士的保护对象。\x02\x03",

            "反正也必须和『结社』\x01",
            "做个了结才行……\x02\x03",

            "就顺便帮你救出\x01",
            "你哥哥他们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        "#1040F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_62(0x146, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #117
        0x146,
        (
            "#212F#5P等、等一下！\x02\x03",

            "#214F为什么我们\x01",
            "非要接受什么游击士的\x01",
            "帮助不可啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1007F哦～『什么游击士』吗。\x02\x03",

            "#1028F这么说的话，\x01",
            "你一个人能救得了他们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x146,
        "#216F#5P唔唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1006F而且我们在逃出\x01",
            "『古罗力亚斯』的时候\x01",
            "不是也受过你们的帮助吗……\x02\x03",

            "就在这个地方\x01",
            "让我还你们一个人情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x146,
        "#214F#5P～～～～～！～～～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        (
            "#1035F#6P乔丝特……\x01",
            "正如艾丝蒂尔所言。\x02\x03",

            "#1040F你一个人待在这里\x01",
            "也解决不了任何问题的。\x02\x03",

            "这点你应该明白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x146,
        "#215F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1040F#6P如果你愿意的话，\x01",
            "就暂时在埃尔赛尤等候好了。\x02\x03",

            "#1035F吉尔他们\x01",
            "应该是被抓到『古罗力亚斯』去了。\x02\x03",

            "照这样子搜索下去的话，\x01",
            "或许可以找到前往\x01",
            "停泊场所的道路也说不定。\x02\x03",

            "#1040F到那时候一定会通知你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x146,
        (
            "#215F#5P………………………………\x02\x03",

            "#413F……我明白了。\x01",
            "既然约修亚这么说的话。\x02\x03",

            "#214F不过，平白接受别人的帮助\x01",
            "会有损我们卡普亚一家的名声的！\x02\x03",

            "搜索也好，修理飞船也好，\x01",
            "请让我也帮忙做点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1016F啊～好的好的，\x01",
            "真是不坦率啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x146,
        (
            "#210F#5P哼、哼……\x02\x03",

            "总比某个喜欢扮好人的\x01",
            "笨女人强吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1019F你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#1052F#6P唉，真是的……\x02\x03",

            "#1048F……虽然不知道是什么原因，\x01",
            "不过你们就不能和睦相处吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x146, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x146)
    Sleep(500)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #130
        0x101,
        "#1007F我说啊，约修亚……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x146, 2)

    ChrTalk(    #131
        0x146,
        "#212F#5P……你怎么能说这种话？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        "#1044F#6P咦……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_483C")

    ChrTalk(    #133
        0x109,
        (
            "#1068F（不好……\x01",
            "  踩到地雷了吗）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493C")

    label("loc_483C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_487B")

    ChrTalk(    #134
        0x104,
        (
            "#035F（哎呀呀……\x01",
            "  好像是踩到地雷了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493C")

    label("loc_487B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48A9")

    ChrTalk(    #135
        0x106,
        "#551F（踩到地雷了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_493C")

    label("loc_48A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48DB")

    ChrTalk(    #136
        0x108,
        "#075F（这下踩到地雷了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_493C")

    label("loc_48DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_490F")

    ChrTalk(    #137
        0x103,
        "#025F（哈……踩到地雷了吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_493C")

    label("loc_490F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_493C")

    ChrTalk(    #138
        0x107,
        "#065F（我、我说哥哥……）\x02",
    )

    CloseMessageWindow()

    label("loc_493C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4971")

    ChrTalk(    #139
        0x105,
        "#1167F（…………………迟钝。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A89")

    label("loc_4971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49A1")

    ChrTalk(    #140
        0x107,
        "#065F（我、我说哥哥……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A89")

    label("loc_49A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D1")

    ChrTalk(    #141
        0x103,
        "#025F（修行远远不够呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A89")

    label("loc_49D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A06")

    ChrTalk(    #142
        0x108,
        (
            "#071F（哎～……\x01",
            "  年轻真好。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A89")

    label("loc_4A06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A4B")

    ChrTalk(    #143
        0x106,
        (
            "#555F（该怎么说呢……\x01",
            "  初生牛犊不畏虎啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A89")

    label("loc_4A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A89")

    ChrTalk(    #144
        0x104,
        (
            "#031F（哈哈哈。\x01",
            "  真是初生牛犊不畏虎啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A89")


    ChrTalk(    #145
        0x101,
        (
            "#1019F喂，乔丝特……\x02\x03",

            "我们现在要不要暂时休战？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x146,
        (
            "#413F#5P……说得也是，\x02\x03",

            "毕竟当前的敌人\x01",
            "并不是彼此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#1048F#6P嗯，那个……\x02\x03",

            "能融洽相处自然是最好\x01",
            "……我说了什么不该说的话了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1001F不，完全没有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x146,
        "#211F#5P大概是心理作用吧～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#1052F#6P是、是吗……\x01",
            "（眼神中看不出笑意……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD2")
    OP_A2(0x22A4)

    label("loc_4BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BE3")
    OP_A2(0x229D)

    label("loc_4BE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF1")

    label("loc_4BF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C02")
    OP_A2(0x22A7)

    label("loc_4C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C13")
    OP_A2(0x22A0)

    label("loc_4C13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C24")
    OP_A2(0x22A2)

    label("loc_4C24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C32")

    label("loc_4C32")

    OP_31(0xA, 0x0, 0x48)
    OP_31(0xA, 0xFE, 0x0)
    OP_41(0xA, 0x6A, 0xFF)
    OP_41(0xA, 0x105, 0xFF)
    OP_41(0xA, 0x126, 0xFF)
    OP_41(0xA, 0x132, 0xFF)
    OP_37(0xA, 0x7F, 0x2)
    OP_41(0xA, 0x29A, 0x0)
    OP_41(0xA, 0x2CB, 0x4)
    OP_41(0xA, 0x298, 0x6)
    OP_35(0xA, 0x0)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #151
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x01",
            "　（离开的人会自动返回埃尔赛尤号。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D55")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D84")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x4, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4D84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB3")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x3, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DE2")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x6, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E11")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x7, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4E11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E40")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x8, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6F")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x4, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E9E")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x3, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4E9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ECD")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x6, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EFC")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x7, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4EFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2B")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x2, 0x8, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F5A")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x3, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4F5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F89")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x6, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4F89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FB8")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x7, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FE7")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x4, 0x8, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_4FE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5016")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x6, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_5016")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5045")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x7, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_5045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5074")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x3, 0x8, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_5074")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A3")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x6, 0x7, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_50A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50D2")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x6, 0x8, 0xA, 0xFFFF)
    Jump("loc_50FE")

    label("loc_50D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50FE")
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x7, 0x8, 0xA, 0xFFFF)

    label("loc_50FE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5801   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3AC3 end

    def Function_17_5124(): pass

    label("Function_17_5124")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_513B")
    Call(0, 20)
    Call(0, 22)

    label("loc_513B")

    OP_D2(0x270003, 0x270007, 0xA)
    OP_D2(0x270013, 0x270017, 0xB)
    OP_D2(0x2700A3, 0x2700A7, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_517E"),
        (3, "loc_518B"),
        (4, "loc_5198"),
        (5, "loc_51A5"),
        (6, "loc_51B2"),
        (7, "loc_51BF"),
        (8, "loc_51CC"),
        (SWITCH_DEFAULT, "loc_51D9"),
    )


    label("loc_517E")

    OP_D2(0x70023, 0x7002B, 0xD)
    Jump("loc_51D9")

    label("loc_518B")

    OP_D2(0x70033, 0x7003B, 0xD)
    Jump("loc_51D9")

    label("loc_5198")

    OP_D2(0x27039B, 0x27039F, 0xD)
    Jump("loc_51D9")

    label("loc_51A5")

    OP_D2(0x70053, 0x7005B, 0xD)
    Jump("loc_51D9")

    label("loc_51B2")

    OP_D2(0x70063, 0x7006B, 0xD)
    Jump("loc_51D9")

    label("loc_51BF")

    OP_D2(0x70073, 0x7007B, 0xD)
    Jump("loc_51D9")

    label("loc_51CC")

    OP_D2(0x270083, 0x270087, 0xD)
    Jump("loc_51D9")

    label("loc_51D9")

    OP_D2(0x270407, 0x27040C, 0xE)
    OP_D2(0x270408, 0x27040D, 0xF)
    OP_6D(59860, 0, 4019, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x10B, 12)
    SetChrChipByIndex(0xF9, 13)
    SetChrChipByIndex(0x9, 14)
    SetChrChipByIndex(0xA, 15)
    SetChrFlags(0x10B, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0x10B, 59020, 200, 3010, 90)
    SetChrPos(0x9, 60220, 200, 4430, 180)
    SetChrPos(0xA, 61850, 200, 4460, 180)
    SetChrPos(0x102, 60040, 200, 1600, 0)
    SetChrPos(0x101, 61850, 200, 1520, 0)
    SetChrPos(0xF9, 62840, 200, 3040, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #152
        0x9,
        (
            "#198F#2P──所以说，\x01",
            "我们打算马上着手进行\x01",
            "『山猫号』的修理工作。\x02\x03",

            "#197F所幸已经找齐了材料，\x01",
            "我想应该会有办法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "#203F#2P机身方面暂且不提，\x01",
            "问题是那个『导力停止现象』。\x02\x03",

            "#206F总之，即使勉强起飞，\x01",
            "也会在离开都市的瞬间坠落吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "如果没有大型的『零力场发生器』，\x01",
            "我想的确会变成那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#1044F#6P要请埃尔赛尤号的\x01",
            "拉赛尔博士帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "#200F#2P嗯，只要在都市里，\x01",
            "导力通讯似乎也可以使用，\x01",
            "必要时我们会联络博士的。\x02\x03",

            "话说回来，你们打算\x01",
            "继续寻找『辉之环』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x102,
        "#1040F#6P嗯，就是这么打算的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1006F#6P那也正是我们\x01",
            "来到这座浮游都市的真正目的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 2)
    Sleep(300)

    ChrTalk(    #159
        0x10B,
        (
            "#213F#5P啊，说到这个，\x01",
            "你们好像曾经提过……\x02\x03",

            "不是要来寻宝什么的吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #160
        0x101,
        (
            "#1019F#6P我说啊……\x01",
            "别把我们和你们混为一谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x9)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #161
        0xA,
        (
            "#200F#2P……那么，乔丝特。\x02\x03",

            "你就继续和约修亚他们\x01",
            "一起行动如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)
    SetChrSubChip(0x10B, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #162
        0x10B,
        "#213F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "#490F#2P修理『山猫号』\x01",
            "有我们几个就足够了。\x02\x03",

            "要说让你负责什么工作的话，\x01",
            "我们还是希望你去收集情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10B,
        "#210F#5P啊，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        (
            "#1035F#6P的确，在这种形势下，\x01",
            "埃尔赛尤和山猫号之间\x01",
            "也需要有一个联络人……\x02\x03",

            "#1040F听起来好像不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1006F#6P嗯，我也有同感。\x02\x03",

            "为了对抗『结社』，\x01",
            "伙伴当然是越多越好。\x02\x03",

            "让乔丝特来进行辅助的话，\x01",
            "完全值得信赖，\x01",
            "这样可就帮我们一个大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 2)
    Sleep(300)

    ChrTalk(    #167
        0x10B,
        "#213F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #168
        0x101,
        "#1004F#6P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x10B,
        (
            "#216F#5P不，这个，怎么说呢……\x02\x03",

            "#215F（……喂，约修亚。\x01",
            "  她说这话是认真的吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        "#1049F#6P（哈哈……她就是那种女孩啊。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x10B,
        "#413F#5P（真让人头疼呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1009F#6P什、什么嘛。\x01",
            "干嘛摆出那副诧异的表情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10B,
        (
            "#210F#5P不，不是诧异的表情，\x01",
            "而是完全的吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1019F#6P什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "#191F#2P哈哈哈。\x01",
            "似乎已经决定了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "#200F#2P那么我们就\x01",
            "返回『山猫号』啦。\x02\x03",

            "乔丝特。\x01",
            "要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10B, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #177
        0x10B,
        (
            "#210F#5P啊，嗯……\x01",
            "大哥你们也要当心哦。\x02\x03",

            "说不定『结社』那些家伙\x01",
            "还会过来袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "#191F#2P哈哈哈，别担心啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        "#200F#2P好了，我们会尽量小心的。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)

    def lambda_5AC4():
        OP_6D(59950, 0, 5310, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5AC4)
    SetChrChipByIndex(0x9, 8)
    SetChrChipByIndex(0xA, 9)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0x9, 59170, 0, 4380, 270)
    SetChrPos(0xA, 62820, 0, 4390, 90)
    OP_0D()
    Sleep(500)

    def lambda_5B18():
        OP_6D(59480, 0, -310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B18)
    OP_43(0x9, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x13)
    SetChrSubChip(0x10B, 1)
    Sleep(50)
    SetChrSubChip(0xF9, 2)
    Sleep(500)
    SetChrSubChip(0x102, 1)
    Sleep(50)
    SetChrSubChip(0x101, 2)
    Sleep(1000)
    SetChrSubChip(0x10B, 0)
    Sleep(50)
    SetChrSubChip(0xF9, 0)
    Sleep(1000)
    SetChrSubChip(0x10B, 2)
    Sleep(50)
    SetChrSubChip(0xF9, 1)
    OP_A2(0x222C)
    OP_28(0x9E, 0x1, 0x100)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x05乔丝特学会了\x07\x02山猫号\x07\x05。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_36(0xA, 0x112)
    OP_BB(0xA, 0x6, 0x112)
    OP_22(0x21E, 0x0, 0x64)
    OP_44(0x9, 0x8)
    OP_44(0xA, 0x9)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x10B, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10B, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10B, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(58080, 0, 600, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 58080, 0, 600, 180)
    SetChrPos(0x1, 58080, 0, 600, 180)
    SetChrPos(0x2, 58080, 0, 600, 180)
    SetChrPos(0x3, 58080, 0, 600, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_5124 end

    def Function_18_5CCF(): pass

    label("Function_18_5CCF")

    OP_8E(0xFE, 0xE060, 0x0, 0xBB8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEAB0, 0x0, 0xFFFFE16A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_5D02():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D02)
    OP_8E(0xFE, 0xEAE2, 0x0, 0xFFFFDCCE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_5CCF end

    def Function_19_5D28(): pass

    label("Function_19_5D28")

    OP_8E(0xFE, 0xFD01, 0x0, 0xD5C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF1EA, 0x0, 0xFFFFE142, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_5D5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D5B)
    OP_8E(0xFE, 0xF1C2, 0x0, 0xFFFFDC4C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_5D28 end

    def Function_20_5D81(): pass

    label("Function_20_5D81")

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
        (0, "loc_5DFB"),
        (1, "loc_5E01"),
        (SWITCH_DEFAULT, "loc_5E07"),
    )


    label("loc_5DFB")

    OP_A2(0x1200)
    Jump("loc_5E07")

    label("loc_5E01")

    OP_A2(0x1201)
    Jump("loc_5E07")

    label("loc_5E07")

    Return()

    # Function_20_5D81 end

    def Function_21_5E08(): pass

    label("Function_21_5E08")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_21_5E08 end

    def Function_22_5E99(): pass

    label("Function_22_5E99")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_22_5E99 end

    SaveToFile()

Try(main)
