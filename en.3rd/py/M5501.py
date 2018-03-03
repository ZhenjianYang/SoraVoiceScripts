from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5501   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5501.x',
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
        'ED6_DT29/CH14540 ._CH',             # 00
        'ED6_DT29/CH14541 ._CH',             # 01
        'ED6_DT29/CH14860 ._CH',             # 02
        'ED6_DT29/CH14861 ._CH',             # 03
        'ED6_DT29/CH15000 ._CH',             # 04
        'ED6_DT29/CH15000 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14860P._CP',             # 02
        'ED6_DT29/CH14861P._CP',             # 03
        'ED6_DT29/CH15000P._CP',             # 04
        'ED6_DT29/CH15000P._CP',             # 05
    )

    DeclMonster(
        X                   = 18160,
        Z                   = 0,
        Y                   = 91630,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25870,
        Z                   = -2000,
        Y                   = 81210,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 44220,
        Z                   = -2000,
        Y                   = 77310,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 52390,
        Z                   = 0,
        Y                   = 54280,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 16750,
        TriggerZ            = 0,
        TriggerY            = 57710,
        TriggerRange        = 1700,
        ActorX              = 16750,
        ActorZ              = 2500,
        ActorY              = 57710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46510,
        TriggerZ            = 0,
        TriggerY            = 67900,
        TriggerRange        = 1700,
        ActorX              = 46510,
        ActorZ              = 2500,
        ActorY              = 67900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53050,
        TriggerZ            = 0,
        TriggerY            = 92420,
        TriggerRange        = 1700,
        ActorX              = 53050,
        ActorZ              = 2500,
        ActorY              = 92420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52950,
        TriggerZ            = 0,
        TriggerY            = 48400,
        TriggerRange        = 1000,
        ActorX              = 52990,
        ActorZ              = 1000,
        ActorY              = 47900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53600,
        TriggerZ            = -2000,
        TriggerY            = 82210,
        TriggerRange        = 1000,
        ActorX              = 54300,
        ActorZ              = -1000,
        ActorY              = 82210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 48210,
        TriggerRange        = 1000,
        ActorX              = 55000,
        ActorZ              = 1000,
        ActorY              = 48210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51000,
        TriggerZ            = 0,
        TriggerY            = 48210,
        TriggerRange        = 1000,
        ActorX              = 51000,
        ActorZ              = 1000,
        ActorY              = 48210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35000,
        TriggerZ            = 0,
        TriggerY            = 92000,
        TriggerRange        = 1000,
        ActorX              = 35000,
        ActorZ              = 1000,
        ActorY              = 92000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_26B",          # 01, 1
        "Function_2_3AF",          # 02, 2
        "Function_3_516",          # 03, 3
        "Function_4_66D",          # 04, 4
        "Function_5_7E1",          # 05, 5
        "Function_6_92F",          # 06, 6
        "Function_7_A6A",          # 07, 7
        "Function_8_D07",          # 08, 8
        "Function_9_EB9",          # 09, 9
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Return()

    # Function_0_26A end

    def Function_1_26B(): pass

    label("Function_1_26B")

    OP_BE(0x0, 0x1, 0x3, 0x190, 0x0, 0x3, -1900, 0, 0, 0, 0, 0)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    OP_72(0x2800, 0x0)
    ExitThread()
    OP_72(0x2801, 0x0)
    ExitThread()
    OP_72(0x2802, 0x0)
    ExitThread()
    OP_72(0x2803, 0x0)
    ExitThread()
    OP_72(0x2804, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_END)), "loc_2E0")
    OP_6F(0x1, 120)
    OP_6F(0x2, 60)

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_END)), "loc_2EE")
    OP_6F(0x2, 160)

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 6)), scpexpr(EXPR_END)), "loc_303")
    OP_6F(0x0, 60)
    OP_6F(0x4, 260)

    label("loc_303")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F")
    OP_6F(0x5, 0)
    Jump("loc_326")

    label("loc_31F")

    OP_6F(0x5, 60)

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x6, 0)
    Jump("loc_33F")

    label("loc_338")

    OP_6F(0x6, 60)

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_6F(0x7, 0)
    Jump("loc_358")

    label("loc_351")

    OP_6F(0x7, 60)

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_6F(0x8, 0)
    Jump("loc_371")

    label("loc_36A")

    OP_6F(0x8, 60)

    label("loc_371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383")
    OP_6F(0x9, 0)
    Jump("loc_38A")

    label("loc_383")

    OP_6F(0x9, 60)

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    OP_64(0x3, 0x1)
    OP_71(0x405, 0x0)
    ExitThread()

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE")
    OP_64(0x4, 0x1)
    OP_71(0x406, 0x0)
    ExitThread()

    label("loc_3AE")

    Return()

    # Function_1_26B end

    def Function_2_3AF(): pass

    label("Function_2_3AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_41D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x74\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2986)
    Jump("loc_485")

    label("loc_41D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x74\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x74\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_485")

    Jump("loc_508")

    label("loc_488")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Judge a dungeon not by the color of its textures, but by the content of\x01",
            "its treasure chests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6B, 0x0)

    label("loc_508")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3AF end

    def Function_3_516(): pass

    label("Function_3_516")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x171, 1)"), scpexpr(EXPR_END)), "loc_584")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x71\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2987)
    Jump("loc_5EC")

    label("loc_584")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x71\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x71\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_5EC")

    Jump("loc_65F")

    label("loc_5EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05And I thought letting you rob me would have been enough to get rid of\x01",
            "you...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6C, 0x0)

    label("loc_65F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_516 end

    def Function_4_66D(): pass

    label("Function_4_66D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_6DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2988)
    Jump("loc_743")

    label("loc_6DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_743")

    Jump("loc_7D3")

    label("loc_746")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05Congratulations! You're the second adventurer to open this chest! This is\x01",
            "why there's nothing left in it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6D, 0x0)

    label("loc_7D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_66D end

    def Function_5_7E1(): pass

    label("Function_5_7E1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_84F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\xFE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2989)
    Jump("loc_8B7")

    label("loc_84F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\xFE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_8B7")

    Jump("loc_921")

    label("loc_8BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05There is nothing left in this chest, mon ami. Am I sure? Tres sure!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6E, 0x0)

    label("loc_921")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7E1 end

    def Function_6_92F(): pass

    label("Function_6_92F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A08")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_99D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\x74\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2996)
    Jump("loc_A05")

    label("loc_99D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\x74\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x74\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_A05")

    Jump("loc_A5C")

    label("loc_A08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05Don't spend it all in one place! Run along, now!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6F, 0x0)

    label("loc_A5C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_92F end

    def Function_7_A6A(): pass

    label("Function_7_A6A")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3A")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B59")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x2964)
    Sleep(500)
    OP_6D(52660, -60, 67850, 1000)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_C37")

    label("loc_B59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C37")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x2965)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0E")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(52800, 0, 47980, 1500)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, 52800, 0, 47980, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_A2(0x2970)
    OP_65(0x3, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_C37")

    label("loc_C0E")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_C37")

    Jump("loc_CFF")

    label("loc_C3A")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 4)), scpexpr(EXPR_END)), "loc_CDF")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_6D(52660, -60, 67850, 1000)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x2964)
    Jump("loc_CFF")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 5)), scpexpr(EXPR_END)), "loc_CFF")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x2965)

    label("loc_CFF")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_7_A6A end

    def Function_8_D07(): pass

    label("Function_8_D07")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4E")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Lower Lever\x01",      # 0
            "Cancel\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4B")
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x2967)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E22")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(53600, -2000, 82210, 1000)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, 53600, -2000, 82210, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_A2(0x2971)
    OP_65(0x4, 0x1)
    Sleep(1500)
    Fade(500)
    Jump("loc_E4B")

    label("loc_E22")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_E4B")

    Jump("loc_EB1")

    label("loc_E4E")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB1")
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    OP_A3(0x2967)

    label("loc_EB1")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_8_D07 end

    def Function_9_EB9(): pass

    label("Function_9_EB9")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F65")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Lower Lever\x01",      # 0
            "Cancel\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F62")
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x104)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2966)

    label("loc_F62")

    Jump("loc_FDE")

    label("loc_F65")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDE")
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 260)
    OP_70(0x4, 0x0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x4)
    OP_A3(0x2966)

    label("loc_FDE")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_9_EB9 end

    SaveToFile()

Try(main)
