from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5612   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5612.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        'ED6_DT29/CH14950 ._CH',             # 00
        'ED6_DT29/CH14951 ._CH',             # 01
        'ED6_DT29/CH14960 ._CH',             # 02
        'ED6_DT29/CH14961 ._CH',             # 03
        'ED6_DT29/CH15160 ._CH',             # 04
        'ED6_DT29/CH15161 ._CH',             # 05
        'ED6_DT29/CH15170 ._CH',             # 06
        'ED6_DT29/CH15171 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH14950P._CP',             # 00
        'ED6_DT29/CH14951P._CP',             # 01
        'ED6_DT29/CH14960P._CP',             # 02
        'ED6_DT29/CH14961P._CP',             # 03
        'ED6_DT29/CH15160P._CP',             # 04
        'ED6_DT29/CH15161P._CP',             # 05
        'ED6_DT29/CH15170P._CP',             # 06
        'ED6_DT29/CH15171P._CP',             # 07
    )

    DeclMonster(
        X                   = -95450,
        Z                   = 0,
        Y                   = 84770,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x282,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46030,
        Z                   = 0,
        Y                   = 79910,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21390,
        Z                   = 0,
        Y                   = 127010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2940,
        Z                   = 0,
        Y                   = 1590,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x283,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14750,
        Z                   = 0,
        Y                   = -4630,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x280,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26480,
        Z                   = 0,
        Y                   = 8660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 62850,
        Z                   = 0,
        Y                   = 58720,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -47920,
        Y                   = 0,
        Z                   = 133000,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -36070,
        Y                   = 0,
        Z                   = 133000,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 79850,
        TriggerZ            = 0,
        TriggerY            = 4770,
        TriggerRange        = 1000,
        ActorX              = 79850,
        ActorZ              = 2000,
        ActorY              = 4770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70570,
        TriggerZ            = 0,
        TriggerY            = 100730,
        TriggerRange        = 800,
        ActorX              = 70570,
        ActorZ              = 1200,
        ActorY              = 100730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37860,
        TriggerZ            = 0,
        TriggerY            = 131790,
        TriggerRange        = 800,
        ActorX              = -37860,
        ActorZ              = 1200,
        ActorY              = 131790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60220,
        TriggerZ            = 4000,
        TriggerY            = 23380,
        TriggerRange        = 1000,
        ActorX              = -60000,
        ActorZ              = 7000,
        ActorY              = 25500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60050,
        TriggerZ            = 0,
        TriggerY            = 29000,
        TriggerRange        = 1000,
        ActorX              = -60050,
        ActorZ              = 1000,
        ActorY              = 29000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56610,
        TriggerZ            = 8000,
        TriggerY            = 35170,
        TriggerRange        = 1000,
        ActorX              = -56610,
        ActorZ              = 9000,
        ActorY              = 35170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92050,
        TriggerZ            = 0,
        TriggerY            = 82040,
        TriggerRange        = 1000,
        ActorX              = -92050,
        ActorZ              = 1000,
        ActorY              = 82040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30,
        TriggerZ            = 0,
        TriggerY            = -4320,
        TriggerRange        = 1000,
        ActorX              = -30,
        ActorZ              = 1000,
        ActorY              = -4320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 65000,
        TriggerZ            = 0,
        TriggerY            = 149000,
        TriggerRange        = 1000,
        ActorX              = 65000,
        ActorZ              = 1000,
        ActorY              = 149000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69000,
        TriggerZ            = 0,
        TriggerY            = 149000,
        TriggerRange        = 1000,
        ActorX              = 69000,
        ActorZ              = 1000,
        ActorY              = 149000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73000,
        TriggerZ            = 0,
        TriggerY            = 149000,
        TriggerRange        = 1000,
        ActorX              = 73000,
        ActorZ              = 1000,
        ActorY              = 149000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_38E",          # 01, 1
        "Function_2_4BB",          # 02, 2
        "Function_3_5E1",          # 03, 3
        "Function_4_707",          # 04, 4
        "Function_5_82D",          # 05, 5
        "Function_6_953",          # 06, 6
        "Function_7_A79",          # 07, 7
        "Function_8_B9F",          # 08, 8
        "Function_9_CC5",          # 09, 9
        "Function_10_F5D",         # 0A, 10
        "Function_11_FFB",         # 0B, 11
        "Function_12_1099",        # 0C, 12
        "Function_13_12B3",        # 0D, 13
        "Function_14_1327",        # 0E, 14
        "Function_15_1570",        # 0F, 15
        "Function_16_1626",        # 10, 16
        "Function_17_16D1",        # 11, 17
        "Function_18_16E4",        # 12, 18
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_38D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_38D")

    Return()

    # Function_0_37A end

    def Function_1_38E(): pass

    label("Function_1_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_39F")

    OP_82(0x84, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3B2")
    OP_82(0x85, 0x0)
    Jump("loc_3B5")

    label("loc_3B2")

    OP_82(0x86, 0x0)

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 1)), scpexpr(EXPR_END)), "loc_3CC")
    OP_64(0x1, 0x1)
    OP_10(0xE, 0x1)
    OP_71(0x1003, 0x0)
    ExitThread()
    Jump("loc_3D5")

    label("loc_3CC")

    OP_10(0xE, 0x0)
    OP_72(0x1003, 0x0)
    ExitThread()

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 2)), scpexpr(EXPR_END)), "loc_3EC")
    OP_64(0x2, 0x1)
    OP_10(0x1, 0x1)
    OP_71(0x100B, 0x0)
    ExitThread()
    Jump("loc_3F5")

    label("loc_3EC")

    OP_10(0x1, 0x0)
    OP_72(0x100B, 0x0)
    ExitThread()

    label("loc_3F5")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D")
    OP_6F(0x13, 0)
    Jump("loc_424")

    label("loc_41D")

    OP_6F(0x13, 60)

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436")
    OP_6F(0x14, 0)
    Jump("loc_43D")

    label("loc_436")

    OP_6F(0x14, 60)

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F")
    OP_6F(0x15, 0)
    Jump("loc_456")

    label("loc_44F")

    OP_6F(0x15, 60)

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468")
    OP_6F(0x16, 0)
    Jump("loc_46F")

    label("loc_468")

    OP_6F(0x16, 60)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_481")
    OP_6F(0x17, 0)
    Jump("loc_488")

    label("loc_481")

    OP_6F(0x17, 60)

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A")
    OP_6F(0x18, 0)
    Jump("loc_4A1")

    label("loc_49A")

    OP_6F(0x18, 60)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3")
    OP_6F(0x19, 0)
    Jump("loc_4BA")

    label("loc_4B3")

    OP_6F(0x19, 60)

    label("loc_4BA")

    Return()

    # Function_1_38E end

    def Function_2_4BB(): pass

    label("Function_2_4BB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DE, 1)"), scpexpr(EXPR_END)), "loc_52F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xDE\x02\x07\x00。\x02",
    )

    Jump("loc_514")

    label("loc_514")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC0)
    Jump("loc_59D")

    label("loc_52F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xDE\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDE\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_57E")

    label("loc_57E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_59D")

    Jump("loc_5D3")

    label("loc_5A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_4BB end

    def Function_3_5E1(): pass

    label("Function_3_5E1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19D, 1)"), scpexpr(EXPR_END)), "loc_655")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x9D\x01\x07\x00。\x02",
    )

    Jump("loc_63A")

    label("loc_63A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC1)
    Jump("loc_6C3")

    label("loc_655")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x9D\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9D\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6A4")

    label("loc_6A4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_6C3")

    Jump("loc_6F9")

    label("loc_6C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5E1 end

    def Function_4_707(): pass

    label("Function_4_707")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x295, 1)"), scpexpr(EXPR_END)), "loc_77B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x95\x02\x07\x00。\x02",
    )

    Jump("loc_760")

    label("loc_760")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC2)
    Jump("loc_7E9")

    label("loc_77B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x95\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x95\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_7CA")

    label("loc_7CA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_7E9")

    Jump("loc_81F")

    label("loc_7EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_81F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_707 end

    def Function_5_82D(): pass

    label("Function_5_82D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_912")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_8A1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_886")

    label("loc_886")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC3)
    Jump("loc_90F")

    label("loc_8A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8F0")

    label("loc_8F0")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_90F")

    Jump("loc_945")

    label("loc_912")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_945")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_82D end

    def Function_6_953(): pass

    label("Function_6_953")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A38")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33D, 1)"), scpexpr(EXPR_END)), "loc_9C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x3D\x03\x07\x00。\x02",
    )

    Jump("loc_9AC")

    label("loc_9AC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC4)
    Jump("loc_A35")

    label("loc_9C7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x3D\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x3D\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_A16")

    label("loc_A16")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_A35")

    Jump("loc_A6B")

    label("loc_A38")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A6B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_953 end

    def Function_7_A79(): pass

    label("Function_7_A79")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x500, 1)"), scpexpr(EXPR_END)), "loc_AED")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x00\x05\x07\x00。\x02",
    )

    Jump("loc_AD2")

    label("loc_AD2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC5)
    Jump("loc_B5B")

    label("loc_AED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x00\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x00\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B3C")

    label("loc_B3C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_B5B")

    Jump("loc_B91")

    label("loc_B5E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A79 end

    def Function_8_B9F(): pass

    label("Function_8_B9F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x578, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C84")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_C13")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_BF8")

    label("loc_BF8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC6)
    Jump("loc_C81")

    label("loc_C13")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_C62")

    label("loc_C62")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_C81")

    Jump("loc_CB7")

    label("loc_C84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CB7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B9F end

    def Function_9_CC5(): pass

    label("Function_9_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D94")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5888)
    Sleep(500)
    Jump("loc_D97")

    label("loc_D94")

    TalkBegin(0xFF)

    label("loc_D97")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_DC1")

    label("loc_DC1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2C")

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

    Jump("loc_E26")

    label("loc_E26")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E43"),
        (1, "loc_EBE"),
        (2, "loc_EED"),
        (SWITCH_DEFAULT, "loc_F1C"),
    )


    label("loc_E43")

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
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F29")

    label("loc_EBE")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #22
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_EEA")

    label("loc_EEA")

    Jump("loc_F29")

    label("loc_EED")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #23
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F19")

    label("loc_F19")

    Jump("loc_F29")

    label("loc_F1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F29")

    label("loc_F29")

    Jump("loc_DD4")

    label("loc_F2C")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    OP_A2(0x259A)
    EventEnd(0x1)
    Jump("loc_F5C")

    label("loc_F59")

    TalkEnd(0xFF)

    label("loc_F5C")

    Return()

    # Function_9_CC5 end

    def Function_10_F5D(): pass

    label("Function_10_F5D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD3")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_64(0x1, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x2B61)
    Jump("loc_FF7")

    label("loc_FD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF7")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_FF7")

    label("loc_FF7")

    TalkEnd(0xFF)
    Return()

    # Function_10_F5D end

    def Function_11_FFB(): pass

    label("Function_11_FFB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1071")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_64(0x2, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x2B62)
    Jump("loc_1095")

    label("loc_1071")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1095")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1095")

    label("loc_1095")

    TalkEnd(0xFF)
    Return()

    # Function_11_FFB end

    def Function_12_1099(): pass

    label("Function_12_1099")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_END)), "loc_10B4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_END)), "loc_10C5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_END)), "loc_10D6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_10D6")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1102"),
        (1, "loc_110F"),
        (3, "loc_116D"),
        (7, "loc_11F1"),
        (SWITCH_DEFAULT, "loc_129B"),
    )


    label("loc_1102")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_129B")

    label("loc_110F")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【什么也不做】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1150"),
        (1, "loc_115D"),
        (SWITCH_DEFAULT, "loc_116A"),
    )


    label("loc_1150")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_116A")

    label("loc_115D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_116A")

    label("loc_116A")

    Jump("loc_129B")

    label("loc_116D")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【什么也不做】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11C7"),
        (1, "loc_11D4"),
        (2, "loc_11E1"),
        (SWITCH_DEFAULT, "loc_11EE"),
    )


    label("loc_11C7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11EE")

    label("loc_11D4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11EE")

    label("loc_11E1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11EE")

    label("loc_11EE")

    Jump("loc_129B")

    label("loc_11F1")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【使用蓝色卡片钥匙】\x01",      # 2
            "【什么也不做】\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1264"),
        (1, "loc_1271"),
        (2, "loc_127E"),
        (3, "loc_128B"),
        (SWITCH_DEFAULT, "loc_1298"),
    )


    label("loc_1264")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1298")

    label("loc_1271")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1298")

    label("loc_127E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1298")

    label("loc_128B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1298")

    label("loc_1298")

    Jump("loc_129B")

    label("loc_129B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_12_1099 end

    def Function_13_12B3(): pass

    label("Function_13_12B3")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
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

    Jump("loc_1310")

    label("loc_1310")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_13_12B3 end

    def Function_14_1327(): pass

    label("Function_14_1327")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -59290, 4000, 22900, 0)
    SetChrPos(0x1, -60910, 4000, 22870, 0)
    SetChrPos(0x2, -59210, 4000, 21270, 0)
    SetChrPos(0x3, -61020, 4000, 21250, 0)
    OP_6D(-60340, 4000, 23500, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FD")
    OP_28(0x17, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_13FD")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1492")

    AnonymousTalk(    #27
        (
            "\x07\x05#40W 汝须将与巨型人偶嬉戏之少女\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W    如此，则『门』将开启。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_1492")


    AnonymousTalk(    #28
        (
            "\x07\x05#40W 汝须将与巨型人偶嬉戏之少女\x01",
            "　　  引领至吾面前。\x01",
            "  然则前方将有试炼降临炼。\x01",
            "#500W\x01",
            "#40W　   如若汝有此等勇气，\x01",
            "     便可穿越此『门』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152A")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1564")
    Call(0, 13)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1561")
    Call(0, 15)

    label("loc_1561")

    Jump("loc_1564")

    label("loc_1564")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_14_1327 end

    def Function_15_1570(): pass

    label("Function_15_1570")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x12, 0)
    OP_70(0x12, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x12)
    Sleep(500)

    def lambda_15D9():
        OP_6B(2830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_15D9)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x22, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1570 end

    def Function_16_1626(): pass

    label("Function_16_1626")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -59290, 4000, 22900, 0)
    SetChrPos(0x1, -60910, 4000, 22870, 0)
    SetChrPos(0x2, -59210, 4000, 21270, 0)
    SetChrPos(0x3, -61020, 4000, 21250, 0)
    OP_6D(-60340, 4000, 23500, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_16_1626 end

    def Function_17_16D1(): pass

    label("Function_17_16D1")

    OP_A3(0x2B64)
    OP_A3(0x2B65)
    OP_A3(0x2B66)
    OP_A2(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_17_16D1 end

    def Function_18_16E4(): pass

    label("Function_18_16E4")

    OP_A3(0x2B64)
    OP_A3(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A2(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_18_16E4 end

    SaveToFile()

Try(main)
