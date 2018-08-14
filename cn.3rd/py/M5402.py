from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5402   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        'ED6_DT29/CH15020 ._CH',             # 00
        'ED6_DT29/CH15021 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH15020P._CP',             # 00
        'ED6_DT29/CH15021P._CP',             # 01
    )

    DeclMonster(
        X                   = -930,
        Z                   = 0,
        Y                   = 20350,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 91770,
        Z                   = 0,
        Y                   = 23560,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 145970,
        Z                   = 0,
        Y                   = -97810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91300,
        Z                   = 0,
        Y                   = 23120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -144320,
        Z                   = 0,
        Y                   = -55930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 110,
        Y                   = -1000,
        Z                   = 82080,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = 1610,
        TriggerZ            = 0,
        TriggerY            = -19170,
        TriggerRange        = 1000,
        ActorX              = 2500,
        ActorZ              = 3000,
        ActorY              = -19000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5030,
        TriggerZ            = 0,
        TriggerY            = 76990,
        TriggerRange        = 1000,
        ActorX              = 5030,
        ActorZ              = 1000,
        ActorY              = 76990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 17980,
        TriggerRange        = 1000,
        ActorX              = -49910,
        ActorZ              = 0,
        ActorY              = 18010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 14500,
        TriggerRange        = 1000,
        ActorX              = -49920,
        ActorZ              = 0,
        ActorY              = 14540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 21480,
        TriggerRange        = 1000,
        ActorX              = -49960,
        ActorZ              = 0,
        ActorY              = 21520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41020,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 41020,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38540,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 38540,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43460,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 43550,
        ActorZ              = 0,
        ActorY              = -23000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -48700,
        TriggerZ            = 0,
        TriggerY            = -27980,
        TriggerRange        = 1000,
        ActorX              = -48040,
        ActorZ              = 0,
        ActorY              = -27980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 23490,
        TriggerRange        = 1000,
        ActorX              = 48450,
        ActorZ              = 0,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47790,
        TriggerZ            = 0,
        TriggerY            = 19970,
        TriggerRange        = 1000,
        ActorX              = 48410,
        ActorZ              = 0,
        ActorY              = 19980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 16490,
        TriggerRange        = 1000,
        ActorX              = 48460,
        ActorZ              = 0,
        ActorY              = 16460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_316",          # 00, 0
        "Function_1_32A",          # 01, 1
        "Function_2_505",          # 02, 2
        "Function_3_5A5",          # 03, 3
        "Function_4_6CB",          # 04, 4
        "Function_5_7F1",          # 05, 5
        "Function_6_917",          # 06, 6
        "Function_7_A6E",          # 07, 7
        "Function_8_B94",          # 08, 8
        "Function_9_CBA",          # 09, 9
        "Function_10_DE0",         # 0A, 10
        "Function_11_F06",         # 0B, 11
        "Function_12_105D",        # 0C, 12
        "Function_13_10D1",        # 0D, 13
        "Function_14_13B5",        # 0E, 14
        "Function_15_146B",        # 0F, 15
        "Function_16_1516",        # 10, 16
        "Function_17_153C",        # 11, 17
    )


    def Function_0_316(): pass

    label("Function_0_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_329")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_329")

    Return()

    # Function_0_316 end

    def Function_1_32A(): pass

    label("Function_1_32A")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_33D")
    OP_82(0x81, 0x0)
    Jump("loc_340")

    label("loc_33D")

    OP_82(0x82, 0x0)

    label("loc_340")

    OP_6F(0x1, 100)
    OP_72(0x201, 0x0)
    ExitThread()
    OP_BE(0x1, 0x1, 0x2, 0x3E8, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_71(0x200, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_71(0x202, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_71(0x203, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_72(0x804, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_71(0x204, 0x0)
    ExitThread()
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C")
    OP_6F(0x1A, 0)
    Jump("loc_423")

    label("loc_41C")

    OP_6F(0x1A, 60)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435")
    OP_6F(0x1B, 0)
    Jump("loc_43C")

    label("loc_435")

    OP_6F(0x1B, 60)

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    OP_6F(0x1C, 0)
    Jump("loc_455")

    label("loc_44E")

    OP_6F(0x1C, 60)

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    OP_6F(0x1D, 0)
    Jump("loc_46E")

    label("loc_467")

    OP_6F(0x1D, 60)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480")
    OP_6F(0x1E, 0)
    Jump("loc_487")

    label("loc_480")

    OP_6F(0x1E, 60)

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    OP_6F(0x1F, 0)
    Jump("loc_4A0")

    label("loc_499")

    OP_6F(0x1F, 60)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2")
    OP_6F(0x20, 0)
    Jump("loc_4B9")

    label("loc_4B2")

    OP_6F(0x20, 60)

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB")
    OP_6F(0x27, 0)
    Jump("loc_4D2")

    label("loc_4CB")

    OP_6F(0x27, 60)

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4")
    OP_6F(0x28, 0)
    Jump("loc_4EB")

    label("loc_4E4")

    OP_6F(0x28, 60)

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD")
    OP_6F(0x29, 0)
    Jump("loc_504")

    label("loc_4FD")

    OP_6F(0x29, 60)

    label("loc_504")

    Return()

    # Function_1_32A end

    def Function_2_505(): pass

    label("Function_2_505")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_6F(0x1A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #0
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_565")

    label("loc_565")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BD0)
    Jump("loc_593")

    label("loc_577")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_593")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_505 end

    def Function_3_5A5(): pass

    label("Function_3_5A5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D6, 1)"), scpexpr(EXPR_END)), "loc_619")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xD6\x02\x07\x00。\x02",
    )

    Jump("loc_5FE")

    label("loc_5FE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD1)
    Jump("loc_687")

    label("loc_619")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xD6\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD6\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_668")

    label("loc_668")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_687")

    Jump("loc_6BD")

    label("loc_68A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6BD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5A5 end

    def Function_4_6CB(): pass

    label("Function_4_6CB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x149, 1)"), scpexpr(EXPR_END)), "loc_73F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x49\x01\x07\x00。\x02",
    )

    Jump("loc_724")

    label("loc_724")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD2)
    Jump("loc_7AD")

    label("loc_73F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x49\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x49\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_78E")

    label("loc_78E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_7AD")

    Jump("loc_7E3")

    label("loc_7B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6CB end

    def Function_5_7F1(): pass

    label("Function_5_7F1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x140, 1)"), scpexpr(EXPR_END)), "loc_865")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\x40\x01\x07\x00。\x02",
    )

    Jump("loc_84A")

    label("loc_84A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD3)
    Jump("loc_8D3")

    label("loc_865")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\x40\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x40\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8B4")

    label("loc_8B4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_8D3")

    Jump("loc_909")

    label("loc_8D6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_909")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7F1 end

    def Function_6_917(): pass

    label("Function_6_917")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A40")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x1E)
    OP_73(0x1E)
    OP_6F(0x1E, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #11
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
    OP_A2(0x2BD4)
    Jump("loc_A5C")

    label("loc_A40")


    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A5C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_917 end

    def Function_7_A6E(): pass

    label("Function_7_A6E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B53")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_AE2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_AC7")

    label("loc_AC7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD5)
    Jump("loc_B50")

    label("loc_AE2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B31")

    label("loc_B31")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_B50")

    Jump("loc_B86")

    label("loc_B53")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B86")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A6E end

    def Function_8_B94(): pass

    label("Function_8_B94")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C79")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E3, 1)"), scpexpr(EXPR_END)), "loc_C08")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\xE3\x02\x07\x00。\x02",
    )

    Jump("loc_BED")

    label("loc_BED")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD6)
    Jump("loc_C76")

    label("loc_C08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\xE3\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xE3\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_C57")

    label("loc_C57")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_C76")

    Jump("loc_CAC")

    label("loc_C79")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CAC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B94 end

    def Function_9_CBA(): pass

    label("Function_9_CBA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_D2E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_D13")

    label("loc_D13")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD7)
    Jump("loc_D9C")

    label("loc_D2E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_D7D")

    label("loc_D7D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_D9C")

    Jump("loc_DD2")

    label("loc_D9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DD2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_CBA end

    def Function_10_DE0(): pass

    label("Function_10_DE0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D3, 1)"), scpexpr(EXPR_END)), "loc_E54")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\xD3\x02\x07\x00。\x02",
    )

    Jump("loc_E39")

    label("loc_E39")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD8)
    Jump("loc_EC2")

    label("loc_E54")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\xD3\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD3\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_EA3")

    label("loc_EA3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_EC2")

    Jump("loc_EF8")

    label("loc_EC5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EF8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_DE0 end

    def Function_11_F06(): pass

    label("Function_11_F06")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x1E)
    OP_73(0x29)
    OP_6F(0x29, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #25
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
    OP_A2(0x2BD9)
    Jump("loc_104B")

    label("loc_102F")


    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_104B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_F06 end

    def Function_12_105D(): pass

    label("Function_12_105D")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
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

    Jump("loc_10BA")

    label("loc_10BA")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_12_105D end

    def Function_13_10D1(): pass

    label("Function_13_10D1")

    TalkBegin(0xFF)
    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -370, 0, -18710, 90)
    SetChrPos(0x1, -250, 0, -20250, 90)
    SetChrPos(0x2, -2290, 0, -18790, 90)
    SetChrPos(0x3, -2260, 0, -20480, 90)
    OP_6D(240, 0, -19190, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(4520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AA")
    OP_28(0x19, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_11AA")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1221")

    AnonymousTalk(    #28
        (
            "\x07\x05#40W     道路既已打开……\x01",
            "#500W\x01",
            "#40W　   穿越此『门』吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D4")

    label("loc_1221")


    AnonymousTalk(    #29
        (
            "\x07\x05#40W  七曜之光，驱散黑暗……\x01",
            "  　其或将成为迷惘时\x01",
            "   指示正确方向之路标。\x01",
            "#500W\x01",
            "#40W  蕴藏七耀光辉之神秘宝珠，\x01",
            "  请将其全数展示于吾面前。\x01",
            "　如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D4")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_130A")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1307")
    Call(0, 14)

    label("loc_1307")

    Jump("loc_13A9")

    label("loc_130A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x295, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x297, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x299, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2CC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A9")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A6")
    Call(0, 14)

    label("loc_13A6")

    Jump("loc_13A9")

    label("loc_13A9")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_13_10D1 end

    def Function_14_13B5(): pass

    label("Function_14_13B5")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2A, 0)
    OP_70(0x2A, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2A)
    Sleep(500)

    def lambda_141E():
        OP_6B(3840, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_141E)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_13B5 end

    def Function_15_146B(): pass

    label("Function_15_146B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -370, 0, -18710, 90)
    SetChrPos(0x1, -250, 0, -20250, 90)
    SetChrPos(0x2, -2290, 0, -18790, 90)
    SetChrPos(0x3, -2260, 0, -20480, 90)
    OP_6D(240, 0, -19190, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(4520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_15_146B end

    def Function_16_1516(): pass

    label("Function_16_1516")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240146, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_16_1516 end

    def Function_17_153C(): pass

    label("Function_17_153C")

    OP_A2(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_17_153C end

    SaveToFile()

Try(main)
