from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7203   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
    )

    DeclMonster(
        X                   = 470,
        Z                   = 8000,
        Y                   = 99600,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20860,
        Z                   = 7950,
        Y                   = 121130,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20490,
        Z                   = 7950,
        Y                   = 79610,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x209,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25630,
        Z                   = 400,
        Y                   = -25450,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1240,
        Z                   = 400,
        Y                   = -24100,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 130,
        Z                   = 0,
        Y                   = 43440,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25120,
        Z                   = -6600,
        Y                   = -25530,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -44950,
        Z                   = -6600,
        Y                   = -15300,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 130,
        TriggerZ            = -7000,
        TriggerY            = -46870,
        TriggerRange        = 1000,
        ActorX              = 130,
        ActorZ              = -5000,
        ActorY              = -46870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47970,
        TriggerZ            = -7050,
        TriggerY            = -47190,
        TriggerRange        = 1000,
        ActorX              = -50000,
        ActorZ              = -4000,
        ActorY              = -47000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21000,
        TriggerZ            = 7900,
        TriggerY            = 121000,
        TriggerRange        = 1000,
        ActorX              = 21000,
        ActorZ              = 9000,
        ActorY              = 121000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21000,
        TriggerZ            = 7900,
        TriggerY            = 79000,
        TriggerRange        = 1000,
        ActorX              = 21000,
        ActorZ              = 9000,
        ActorY              = 79000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47920,
        TriggerZ            = -6500,
        TriggerY            = -660,
        TriggerRange        = 1000,
        ActorX              = -47920,
        ActorZ              = -5600,
        ActorY              = -660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14220,
        TriggerZ            = 300,
        TriggerY            = -19440,
        TriggerRange        = 1000,
        ActorX              = -14220,
        ActorZ              = 1400,
        ActorY              = -19440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 45000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 45000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29250,
        TriggerZ            = 400,
        TriggerY            = 20390,
        TriggerRange        = 1000,
        ActorX              = 29250,
        ActorZ              = 1400,
        ActorY              = 20390,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31A",          # 00, 0
        "Function_1_39A",          # 01, 1
        "Function_2_4AB",          # 02, 2
        "Function_3_602",          # 03, 3
        "Function_4_728",          # 04, 4
        "Function_5_84E",          # 05, 5
        "Function_6_974",          # 06, 6
        "Function_7_A9A",          # 07, 7
        "Function_8_BC0",          # 08, 8
        "Function_9_CC2",          # 09, 9
        "Function_10_F5A",         # 0A, 10
        "Function_11_1038",        # 0B, 11
        "Function_12_1116",        # 0C, 12
        "Function_13_11F4",        # 0D, 13
        "Function_14_12D2",        # 0E, 14
        "Function_15_13B0",        # 0F, 15
        "Function_16_148E",        # 10, 16
        "Function_17_154A",        # 11, 17
        "Function_18_1606",        # 12, 18
        "Function_19_16C2",        # 13, 19
        "Function_20_177E",        # 14, 20
        "Function_21_183A",        # 15, 21
        "Function_22_18F6",        # 16, 22
        "Function_23_1A0C",        # 17, 23
        "Function_24_1A5A",        # 18, 24
        "Function_25_1ACE",        # 19, 25
        "Function_26_1C9B",        # 1A, 26
        "Function_27_1D54",        # 1B, 27
    )


    def Function_0_31A(): pass

    label("Function_0_31A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_346"),
        (101, "loc_34D"),
        (102, "loc_354"),
        (103, "loc_35B"),
        (104, "loc_362"),
        (105, "loc_369"),
        (SWITCH_DEFAULT, "loc_370"),
    )


    label("loc_346")

    Event(0, 10)
    Jump("loc_370")

    label("loc_34D")

    Event(0, 11)
    Jump("loc_370")

    label("loc_354")

    Event(0, 12)
    Jump("loc_370")

    label("loc_35B")

    Event(0, 13)
    Jump("loc_370")

    label("loc_362")

    Event(0, 14)
    Jump("loc_370")

    label("loc_369")

    Event(0, 15)
    Jump("loc_370")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_386")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 27)
    Jump("loc_399")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_399")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_399")

    Return()

    # Function_0_31A end

    def Function_1_39A(): pass

    label("Function_1_39A")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE98A0, 0x23008E)
    OP_1B(0x0, 0x0, 0x10)
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x14)
    OP_1B(0x5, 0x0, 0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_3D7")
    OP_71(0x401, 0x0)
    ExitThread()

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_3E8")

    OP_82(0x89, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3FB")
    OP_82(0x8A, 0x0)
    Jump("loc_3FE")

    label("loc_3FB")

    OP_82(0x8B, 0x0)

    label("loc_3FE")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426")
    OP_6F(0x4, 0)
    Jump("loc_42D")

    label("loc_426")

    OP_6F(0x4, 60)

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F")
    OP_6F(0x5, 0)
    Jump("loc_446")

    label("loc_43F")

    OP_6F(0x5, 60)

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458")
    OP_6F(0x6, 0)
    Jump("loc_45F")

    label("loc_458")

    OP_6F(0x6, 60)

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471")
    OP_6F(0x7, 0)
    Jump("loc_478")

    label("loc_471")

    OP_6F(0x7, 60)

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    OP_6F(0x8, 0)
    Jump("loc_491")

    label("loc_48A")

    OP_6F(0x8, 60)

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3")
    OP_6F(0x9, 0)
    Jump("loc_4AA")

    label("loc_4A3")

    OP_6F(0x9, 60)

    label("loc_4AA")

    Return()

    # Function_1_39A end

    def Function_2_4AB(): pass

    label("Function_2_4AB")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2A98)
    Jump("loc_5F0")

    label("loc_5D4")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5F0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_4AB end

    def Function_3_602(): pass

    label("Function_3_602")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x174, 1)"), scpexpr(EXPR_END)), "loc_676")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x74\x01\x07\x00。\x02",
    )

    Jump("loc_65B")

    label("loc_65B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A99)
    Jump("loc_6E4")

    label("loc_676")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\x74\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x74\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6C5")

    label("loc_6C5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_6E4")

    Jump("loc_71A")

    label("loc_6E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_71A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_602 end

    def Function_4_728(): pass

    label("Function_4_728")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A7, 1)"), scpexpr(EXPR_END)), "loc_79C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xA7\x01\x07\x00。\x02",
    )

    Jump("loc_781")

    label("loc_781")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A9A)
    Jump("loc_80A")

    label("loc_79C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xA7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_7EB")

    label("loc_7EB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_80A")

    Jump("loc_840")

    label("loc_80D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_840")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_728 end

    def Function_5_84E(): pass

    label("Function_5_84E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4D1, 1)"), scpexpr(EXPR_END)), "loc_8C2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xD1\x04\x07\x00。\x02",
    )

    Jump("loc_8A7")

    label("loc_8A7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A9B)
    Jump("loc_930")

    label("loc_8C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xD1\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD1\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_911")

    label("loc_911")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_930")

    Jump("loc_966")

    label("loc_933")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_966")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_84E end

    def Function_6_974(): pass

    label("Function_6_974")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17B, 1)"), scpexpr(EXPR_END)), "loc_9E8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x7B\x01\x07\x00。\x02",
    )

    Jump("loc_9CD")

    label("loc_9CD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A9C)
    Jump("loc_A56")

    label("loc_9E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x7B\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7B\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_A37")

    label("loc_A37")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_A56")

    Jump("loc_A8C")

    label("loc_A59")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_974 end

    def Function_7_A9A(): pass

    label("Function_7_A9A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x553, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12F, 1)"), scpexpr(EXPR_END)), "loc_B0E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\x2F\x01\x07\x00。\x02",
    )

    Jump("loc_AF3")

    label("loc_AF3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A9D)
    Jump("loc_B7C")

    label("loc_B0E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\x2F\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x2F\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B5D")

    label("loc_B5D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_B7C")

    Jump("loc_BB2")

    label("loc_B7F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BB2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A9A end

    def Function_8_BC0(): pass

    label("Function_8_BC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(0, 14000, -26220, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(0, 0)
    OP_6E(290, 0)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)

    def lambda_C23():
        OP_6D(0, -3950, -27220, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C23)

    def lambda_C3B():
        OP_67(0, 2600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C3B)

    def lambda_C53():
        OP_6B(5000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_C53)

    def lambda_C63():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C63)

    def lambda_C73():
        OP_6E(300, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C73)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(1000)

    def lambda_C97():
        OP_6B(4500, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_C97)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    OP_A2(0x2505)
    OP_A2(0x2507)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_BC0 end

    def Function_9_CC2(): pass

    label("Function_9_CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D91")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(4352)
    Sleep(500)
    Jump("loc_D94")

    label("loc_D91")

    TalkBegin(0xFF)

    label("loc_D94")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_DBE")

    label("loc_DBE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F29")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_E23")

    label("loc_E23")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E40"),
        (1, "loc_EBB"),
        (2, "loc_EEA"),
        (SWITCH_DEFAULT, "loc_F19"),
    )


    label("loc_E40")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F26")

    label("loc_EBB")

    OP_A9(0x22)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_EE7")

    label("loc_EE7")

    Jump("loc_F26")

    label("loc_EEA")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F16")

    label("loc_F16")

    Jump("loc_F26")

    label("loc_F19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F26")

    label("loc_F26")

    Jump("loc_DD1")

    label("loc_F29")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F56")
    OP_A2(0x2594)
    EventEnd(0x1)
    Jump("loc_F59")

    label("loc_F56")

    TalkEnd(0xFF)

    label("loc_F59")

    Return()

    # Function_9_CC2 end

    def Function_10_F5A(): pass

    label("Function_10_F5A")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -21110, 8050, 121150, 135)
    SetChrPos(0x1, -21110, 8050, 121150, 135)
    SetChrPos(0x2, -21110, 8050, 121150, 135)
    SetChrPos(0x3, -21110, 8050, 121150, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21110, 8050, 121150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_F5A end

    def Function_11_1038(): pass

    label("Function_11_1038")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -21170, 8050, 78730, 45)
    SetChrPos(0x1, -21170, 8050, 78730, 45)
    SetChrPos(0x2, -21170, 8050, 78730, 45)
    SetChrPos(0x3, -21170, 8050, 78730, 45)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21170, 8050, 78730, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_1038 end

    def Function_12_1116(): pass

    label("Function_12_1116")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -43820, -6950, 43870, 135)
    SetChrPos(0x1, -43820, -6950, 43870, 135)
    SetChrPos(0x2, -43820, -6950, 43870, 135)
    SetChrPos(0x3, -43820, -6950, 43870, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -43820, -6950, 43870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_1116 end

    def Function_13_11F4(): pass

    label("Function_13_11F4")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 46820, -3950, -46800, 315)
    SetChrPos(0x1, 46820, -3950, -46800, 315)
    SetChrPos(0x2, 46820, -3950, -46800, 315)
    SetChrPos(0x3, 46820, -3950, -46800, 315)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 46820, -3950, -46800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_11F4 end

    def Function_14_12D2(): pass

    label("Function_14_12D2")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 150, 50, 71700, 180)
    SetChrPos(0x1, 150, 50, 71700, 180)
    SetChrPos(0x2, 150, 50, 71700, 180)
    SetChrPos(0x3, 150, 50, 71700, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 150, 50, 71700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_14_12D2 end

    def Function_15_13B0(): pass

    label("Function_15_13B0")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 240, 1750, -230, 180)
    SetChrPos(0x1, 240, 1750, -230, 180)
    SetChrPos(0x2, 240, 1750, -230, 180)
    SetChrPos(0x3, 240, 1750, -230, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 240, 1750, -230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_15_13B0 end

    def Function_16_148E(): pass

    label("Function_16_148E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -21110, 8050, 121150, 315)
    SetChrPos(0x2, -21110, 8050, 121150, 315)
    SetChrPos(0x1, -21110, 8050, 121150, 315)
    SetChrPos(0x0, -21110, 8050, 121150, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21110, 8050, 121150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7202   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_16_148E end

    def Function_17_154A(): pass

    label("Function_17_154A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -21170, 8050, 78730, 225)
    SetChrPos(0x2, -21170, 8050, 78730, 225)
    SetChrPos(0x1, -21170, 8050, 78730, 225)
    SetChrPos(0x0, -21170, 8050, 78730, 225)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21170, 8050, 78730, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7202   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_154A end

    def Function_18_1606(): pass

    label("Function_18_1606")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -43820, -6950, 43870, 315)
    SetChrPos(0x2, -43820, -6950, 43870, 315)
    SetChrPos(0x1, -43820, -6950, 43870, 315)
    SetChrPos(0x0, -43820, -6950, 43870, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -43820, -6950, 43870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7202   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1606 end

    def Function_19_16C2(): pass

    label("Function_19_16C2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 46820, -3950, -46800, 135)
    SetChrPos(0x2, 46820, -3950, -46800, 135)
    SetChrPos(0x1, 46820, -3950, -46800, 135)
    SetChrPos(0x0, 46820, -3950, -46800, 135)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 46820, -3950, -46800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7202   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_16C2 end

    def Function_20_177E(): pass

    label("Function_20_177E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 150, 50, 71700, 0)
    SetChrPos(0x2, 150, 50, 71700, 0)
    SetChrPos(0x1, 150, 50, 71700, 0)
    SetChrPos(0x0, 150, 50, 71700, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 150, 50, 71700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7202   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_20_177E end

    def Function_21_183A(): pass

    label("Function_21_183A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 240, 1750, -230, 0)
    SetChrPos(0x2, 240, 1750, -230, 0)
    SetChrPos(0x1, 240, 1750, -230, 0)
    SetChrPos(0x0, 240, 1750, -230, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 240, 1750, -230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 23)
    NewScene("ED6_DT21/M7204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_183A end

    def Function_22_18F6(): pass

    label("Function_22_18F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_191F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1913():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1913)

    label("loc_191F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1948")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_193C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_193C)

    label("loc_1948")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1971")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1965():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1965)

    label("loc_1971")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199A")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_198E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_198E)

    label("loc_199A")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C6")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_19C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DD")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_19DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_19F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A0B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1A0B")

    Return()

    # Function_22_18F6 end

    def Function_23_1A0C(): pass

    label("Function_23_1A0C")


    def lambda_1A12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A12)

    def lambda_1A24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A24)

    def lambda_1A36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A36)

    def lambda_1A48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A48)
    Sleep(1000)
    Return()

    # Function_23_1A0C end

    def Function_24_1A5A(): pass

    label("Function_24_1A5A")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
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

    Jump("loc_1AB7")

    label("loc_1AB7")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_24_1A5A end

    def Function_25_1ACE(): pass

    label("Function_25_1ACE")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -46940, -7050, -46240, 270)
    SetChrPos(0x1, -46810, -7050, -47720, 270)
    SetChrPos(0x2, -45110, -7050, -45890, 270)
    SetChrPos(0x3, -44770, -7050, -47620, 270)
    OP_6D(-48210, -7050, -47270, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA4")
    OP_28(0x1F, 0x4, 0x2)
    OP_82(0x8A, 0x2)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1BA4")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #21
        (
            "\x07\x05#40W　   应选左或是右……\x01",
            "　　　 汝等之前途\x01",
            "   惟有『卡片』知晓……\x01",
            "#500W\x01",
            "#40W　  若要通过此『门』，\x01",
            "　请出示掌管命运之『卡片』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8F")
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8C")
    Call(0, 26)

    label("loc_1C8C")

    Jump("loc_1C8F")

    label("loc_1C8F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_25_1ACE end

    def Function_26_1C9B(): pass

    label("Function_26_1C9B")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)

    def lambda_1D04():
        OP_6B(4200, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1D04)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_23(0x85)
    OP_E3(0x0, 0xB, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_1C9B end

    def Function_27_1D54(): pass

    label("Function_27_1D54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -46940, -7050, -46240, 270)
    SetChrPos(0x1, -46810, -7050, -47720, 270)
    SetChrPos(0x2, -45110, -7050, -45890, 270)
    SetChrPos(0x3, -44770, -7050, -47620, 270)
    OP_6D(-48210, -7050, -47270, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_27_1D54 end

    SaveToFile()

Try(main)
