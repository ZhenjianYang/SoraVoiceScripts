from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0100.x',
        MapIndex            = 14,
        MapDefaultBGM       = "ed60030",
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
        'キラーキャンサー',                     # 9
        'キラーキャンサー',                     # 10
        'キラーキャンサー',                     # 11
        'キラーキャンサー',                     # 12
        'キラーキャンサー',                     # 13
        'キラーキャンサー',                     # 14
    )

    DeclEntryPoint(
        Unknown_00              = 25000,
        Unknown_04              = 0,
        Unknown_08              = 9000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 14,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10000 ._CH',             # 00
        'ED6_DT09/CH10001 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT09/CH10000P._CP',             # 00
        'ED6_DT09/CH10001P._CP',             # 01
    )

    DeclMonster(
        X                   = 114000,
        Z                   = -500,
        Y                   = 80000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 108000,
        Z                   = 0,
        Y                   = 54000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105000,
        Z                   = 0,
        Y                   = 16000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 129090,
        Z                   = 1000,
        Y                   = 12770,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 93190,
        Z                   = 0,
        Y                   = 86160,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84390,
        Z                   = 1000,
        Y                   = 32040,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 14000,
        TriggerZ            = 1000,
        TriggerY            = 31800,
        TriggerRange        = 1000,
        ActorX              = 14000,
        ActorZ              = 1000,
        ActorY              = 31800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_33E",          # 02, 2
        "Function_3_4BB",          # 03, 3
        "Function_4_4FC",          # 04, 4
        "Function_5_663",          # 05, 5
        "Function_6_84A",          # 06, 6
        "Function_7_9A8",          # 07, 7
        "Function_8_AFF",          # 08, 8
        "Function_9_B5B",          # 09, 9
    )


    def Function_0_186(): pass

    label("Function_0_186")

    OP_A2(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    Return()

    # Function_0_186 end

    def Function_1_190(): pass

    label("Function_1_190")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    OP_71(0x2D, 0x4)
    OP_71(0x2E, 0x4)
    OP_71(0x2F, 0x4)
    OP_71(0x30, 0x4)
    OP_71(0x31, 0x4)
    OP_71(0x32, 0x4)
    OP_78(0x80, 0x80, 0x80)
    OP_79(0xFF, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x1, 0x0)
    Jump("loc_2F5")

    label("loc_2AC")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_306")
    OP_6F(0x0, 0)
    Jump("loc_325")

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_317")
    OP_6F(0x0, 330)
    Jump("loc_325")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_325")
    OP_6F(0x0, 900)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_336")
    OP_6F(0x3, 25)
    Jump("loc_33D")

    label("loc_336")

    OP_6F(0x3, 0)

    label("loc_33D")

    Return()

    # Function_1_190 end

    def Function_2_33E(): pass

    label("Function_2_33E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A5")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4A5")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4A5")

    label("loc_395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4A5")

    label("loc_3C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4A5")

    label("loc_3E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4A5")

    label("loc_3F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4A5")

    label("loc_412")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4A5")

    label("loc_42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_444")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4A5")

    label("loc_444")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4A5")

    label("loc_45D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4A5")

    label("loc_476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4A5")

    label("loc_48F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_4BA")

    Return()

    # Function_2_33E end

    def Function_3_4BB(): pass

    label("Function_3_4BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05The elevator is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_4BB end

    def Function_4_4FC(): pass

    label("Function_4_4FC")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride Elevator\x01",      # 0
            "Don't Ride\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56A")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_56A")

    Fade(1000)
    SetChrPos(0x0, 128580, 50, 77550, 0)
    SetChrPos(0x1, 129580, 50, 77550, 0)
    SetChrPos(0x2, 128580, 50, 76780, 0)
    SetChrPos(0x3, 129580, 50, 76780, 0)
    OP_6D(129020, 50, 77590, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x2, 0x168)
    OP_73(0x2)
    OP_6F(0x2, 360)
    Fade(1000)
    OP_6F(0x1, 120)
    Sleep(120)
    OP_6D(54110, 50, 57680, 0)
    SetChrPos(0x0, 53570, -6000, 57550, 180)
    SetChrPos(0x1, 54570, -6000, 57550, 180)
    SetChrPos(0x2, 53570, -6000, 56780, 180)
    SetChrPos(0x3, 54570, -6000, 56780, 180)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_6F(0x1, 0)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4FC end

    def Function_5_663(): pass

    label("Function_5_663")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride Trolley\x01",      # 0
            "Don't Ride\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C6")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_6C6")

    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 15900, 400, 32299, 0)
    SetChrPos(0x1, 15900, 400, 32299, 0)
    SetChrPos(0x2, 15900, 400, 32299, 0)
    SetChrPos(0x3, 15900, 400, 32299, 0)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BD")
    OP_A3(0x1)
    OP_A2(0x2)
    OP_A3(0x3)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14A)
    OP_73(0x0)
    OP_6F(0x0, 330)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34200, 100, 61400, 315)
    SetChrPos(0x1, 34200, 100, 61400, 315)
    SetChrPos(0x2, 34200, 100, 61400, 315)
    SetChrPos(0x3, 34200, 100, 61400, 315)
    Jump("loc_842")

    label("loc_7BD")

    OP_A3(0x1)
    OP_A3(0x2)
    OP_A2(0x3)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x384)
    OP_73(0x0)
    OP_6F(0x0, 900)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50500, 0, 51900, 45)
    SetChrPos(0x1, 50500, 0, 51900, 45)
    SetChrPos(0x2, 50500, 0, 51900, 45)
    SetChrPos(0x3, 50500, 0, 51900, 45)

    label("loc_842")

    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_5_663 end

    def Function_6_84A(): pass

    label("Function_6_84A")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride Trolley\x01",      # 0
            "Don't Ride\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AD")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_8AD")

    OP_A2(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    SetMapFlags(0x1)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34800, 400, 59200, 225)
    SetChrPos(0x1, 34800, 400, 59200, 225)
    SetChrPos(0x2, 34800, 400, 59200, 225)
    SetChrPos(0x3, 34800, 400, 59200, 225)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 330)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_6F(0x0, 0)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_84A end

    def Function_7_9A8(): pass

    label("Function_7_9A8")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride Trolley\x01",      # 0
            "Don't Ride\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0B")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_A0B")

    OP_A2(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50200, 400, 49900, 270)
    SetChrPos(0x1, 50200, 400, 49900, 270)
    SetChrPos(0x2, 50200, 400, 49900, 270)
    SetChrPos(0x3, 50200, 400, 49900, 270)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 900)
    OP_70(0x0, 0x1F4)
    OP_73(0x0)
    OP_6F(0x0, 500)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_9A8 end

    def Function_8_AFF(): pass

    label("Function_8_AFF")

    SetMapFlags(0x80)
    Sleep(30)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05The lever is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_AFF end

    def Function_9_B5B(): pass

    label("Function_9_B5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_D7C")

    label("loc_BC1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_70(0x33, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_D61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_D7B")

    Return()

    label("loc_D7C")

    Return()

    # Function_9_B5B end

    SaveToFile()

Try(main)
