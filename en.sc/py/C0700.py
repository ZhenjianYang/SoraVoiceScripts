from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        'ED6_DT29/CH12590 ._CH',             # 00
        'ED6_DT29/CH12591 ._CH',             # 01
        'ED6_DT29/CH12600 ._CH',             # 02
        'ED6_DT29/CH12601 ._CH',             # 03
        'ED6_DT29/CH12610 ._CH',             # 04
        'ED6_DT29/CH12611 ._CH',             # 05
        'ED6_DT29/CH12620 ._CH',             # 06
        'ED6_DT29/CH12621 ._CH',             # 07
        'ED6_DT29/CH12630 ._CH',             # 08
        'ED6_DT29/CH12631 ._CH',             # 09
        'ED6_DT29/CH12640 ._CH',             # 0A
        'ED6_DT29/CH12641 ._CH',             # 0B
        'ED6_DT29/CH12650 ._CH',             # 0C
        'ED6_DT29/CH12651 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12590P._CP',             # 00
        'ED6_DT29/CH12591P._CP',             # 01
        'ED6_DT29/CH12600P._CP',             # 02
        'ED6_DT29/CH12601P._CP',             # 03
        'ED6_DT29/CH12610P._CP',             # 04
        'ED6_DT29/CH12611P._CP',             # 05
        'ED6_DT29/CH12620P._CP',             # 06
        'ED6_DT29/CH12621P._CP',             # 07
        'ED6_DT29/CH12630P._CP',             # 08
        'ED6_DT29/CH12631P._CP',             # 09
        'ED6_DT29/CH12640P._CP',             # 0A
        'ED6_DT29/CH12641P._CP',             # 0B
        'ED6_DT29/CH12650P._CP',             # 0C
        'ED6_DT29/CH12651P._CP',             # 0D
    )

    DeclMonster(
        X                   = -7290,
        Z                   = -7200,
        Y                   = -490,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8128,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7690,
        Z                   = -7200,
        Y                   = 490,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8129,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -20,
        TriggerZ            = -7650,
        TriggerY            = -650,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -7650,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_176",          # 00, 0
        "Function_1_1A4",          # 01, 1
        "Function_2_208",          # 02, 2
        "Function_3_352",          # 03, 3
        "Function_4_9E6",          # 04, 4
        "Function_5_A51",          # 05, 5
        "Function_6_ABC",          # 06, 6
        "Function_7_B27",          # 07, 7
        "Function_8_B92",          # 08, 8
        "Function_9_C18",          # 09, 9
        "Function_10_CA7",         # 0A, 10
        "Function_11_E95",         # 0B, 11
        "Function_12_F84",         # 0C, 12
        "Function_13_1009",        # 0D, 13
        "Function_14_108E",        # 0E, 14
        "Function_15_1113",        # 0F, 15
        "Function_16_1198",        # 10, 16
        "Function_17_1293",        # 11, 17
        "Function_18_12F1",        # 12, 18
        "Function_19_13D0",        # 13, 19
        "Function_20_14AF",        # 14, 20
        "Function_21_14FD",        # 15, 21
    )


    def Function_0_176(): pass

    label("Function_0_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185")
    Event(0, 3)
    Jump("loc_1A3")

    label("loc_185")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_195"),
        (101, "loc_19C"),
        (SWITCH_DEFAULT, "loc_1A3"),
    )


    label("loc_195")

    Event(0, 10)
    Jump("loc_1A3")

    label("loc_19C")

    Event(0, 16)
    Jump("loc_1A3")

    label("loc_1A3")

    Return()

    # Function_0_176 end

    def Function_1_1A4(): pass

    label("Function_1_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6")
    OP_6F(0x1, 0)
    Jump("loc_1BD")

    label("loc_1B6")

    OP_6F(0x1, 60)

    label("loc_1BD")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    OP_1B(0x0, 0x0, 0xB)
    OP_1B(0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 0)), scpexpr(EXPR_END)), "loc_1FB")
    SetChrFlags(0x8, 0x80)

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 1)), scpexpr(EXPR_END)), "loc_207")
    SetChrFlags(0x9, 0x80)

    label("loc_207")

    Return()

    # Function_1_1A4 end

    def Function_2_208(): pass

    label("Function_2_208")

    OP_EA(0x2, 0x14, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_279")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F00)
    Jump("loc_2DD")

    label("loc_279")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_2DD")

    Jump("loc_344")

    label("loc_2E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05I suppose I didn't NEED that, but I mean, you\x01",
            "could have asked first.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_344")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_208 end

    def Function_3_352(): pass

    label("Function_3_352")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_369")
    Call(0, 8)
    Call(0, 9)

    label("loc_369")

    OP_6D(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(800)

    def lambda_463():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_463)
    OP_43(0x102, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    Sleep(600)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#1004F#6PWhat in the?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x0)

    ChrTalk(    #4
        0x102,
        "#1044F#4PThis is...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x1, 0x3E8)
    OP_DE("Esmelas Tower")
    OP_6D(3520, 11180, 56940, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)

    def lambda_553():
        OP_6D(-170, 600, -78050, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_553)

    def lambda_56B():
        OP_67(0, 7500, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56B)

    def lambda_583():
        OP_6B(3000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_583)

    def lambda_593():
        OP_6C(315000, 15000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593)

    def lambda_5A3():
        OP_6E(262, 15000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A3)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#1020F#6PW-Wait a second!\x02\x03",

            "We went into the tower,\x01",
            "didn't we?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661")

    ChrTalk(    #6
        0x109,
        (
            "#1065F#6PSpatial translocation...\x02\x03",

            "#1063FLooks like we got sent somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_661")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E2")

    ChrTalk(    #7
        0x107,
        (
            "#065F#6PC-Could this be spatial translocation...?\x02\x03",

            "Umm, I think we were sent\x01",
            "somewhere else by that field!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(    #8
        0x105,
        (
            "#047F#6PCould this be spatial translocation...?\x02\x03",

            "#042FI believe we were sent elsewhere\x01",
            "after passing through that...field.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_807")

    ChrTalk(    #9
        0x108,
        (
            "#074F#6P 'As the soul moves, so does the body'...\x02\x03",

            "#072FThat kekkai, or 'field' as you might\x01",
            "call it, sent us somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_807")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_880")

    ChrTalk(    #10
        0x103,
        (
            "#026F#6PWe were transported somehow...\x02\x03",

            "#022FWe went somewhere else after\x01",
            "passing through that field.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x101, 180, 600)

    ChrTalk(    #11
        0x101,
        (
            "#1019F#4POh, come on, this is getting ridiculous!\x02\x03",

            "#1020FI mean, doesn't that mean there's\x01",
            "no way to climb the tower...?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #12
        0x102,
        (
            "#1035FCalm down, Estelle.\x02\x03",

            "#1040FIf Bleublanc came in here,\x01",
            "there must be some way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #13
        0x101,
        (
            "#1007F#4PYou're right...\x02\x03",

            "#1002FOkay! Let's go! ...Carefully!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E05)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_352 end

    def Function_4_9E6(): pass

    label("Function_4_9E6")


    def lambda_9EC():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EC)

    def lambda_A06():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A06)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_A31():
        OP_8F(0xFE, 0x262, 0x258, 0xFFFECFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A31)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_9E6 end

    def Function_5_A51(): pass

    label("Function_5_A51")


    def lambda_A57():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A57)

    def lambda_A71():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A71)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_A9C():
        OP_8F(0xFE, 0xFFFFFE2A, 0x258, 0xFFFECEF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A9C)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_A51 end

    def Function_6_ABC(): pass

    label("Function_6_ABC")


    def lambda_AC2():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AC2)

    def lambda_ADC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADC)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_B07():
        OP_8F(0xFE, 0x276, 0x2EE, 0xFFFECA32, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B07)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_ABC end

    def Function_7_B27(): pass

    label("Function_7_B27")


    def lambda_B2D():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B2D)

    def lambda_B47():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B47)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_B72():
        OP_8F(0xFE, 0xFFFFFDE4, 0x2EE, 0xFFFECA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B72)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_B27 end

    def Function_8_B92(): pass

    label("Function_8_B92")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C0B"),
        (1, "loc_C11"),
        (SWITCH_DEFAULT, "loc_C17"),
    )


    label("loc_C0B")

    OP_A2(0x1200)
    Jump("loc_C17")

    label("loc_C11")

    OP_A2(0x1201)
    Jump("loc_C17")

    label("loc_C17")

    Return()

    # Function_8_B92 end

    def Function_9_C18(): pass

    label("Function_9_C18")

    FadeToDark(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_C18 end

    def Function_10_CA7(): pass

    label("Function_10_CA7")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x1, 0x3E8)
    OP_DE("Esmelas Tower")
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(800)

    def lambda_DC6():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DC6)
    OP_43(0x102, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 610, 600, -77870, 0)
    SetChrPos(0x1, 610, 600, -77870, 0)
    SetChrPos(0x2, 610, 600, -77870, 0)
    SetChrPos(0x3, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_CA7 end

    def Function_11_E95(): pass

    label("Function_11_E95")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-600, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(219000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 680, 700, -81310, 180)
    SetChrPos(0x102, -330, 700, -81100, 180)
    SetChrPos(0xF8, 910, 750, -79600, 180)
    SetChrPos(0xF9, -270, 750, -79450, 180)
    OP_43(0x101, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xD)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xE)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R0303   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_11_E95 end

    def Function_12_F84(): pass

    label("Function_12_F84")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_FC9():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC9)

    def lambda_FE3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE3)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_F84 end

    def Function_13_1009(): pass

    label("Function_13_1009")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_104E():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_104E)

    def lambda_1068():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1068)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_1009 end

    def Function_14_108E(): pass

    label("Function_14_108E")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_10D3():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D3)

    def lambda_10ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10ED)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_14_108E end

    def Function_15_1113(): pass

    label("Function_15_1113")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1158():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1158)

    def lambda_1172():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1172)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_15_1113 end

    def Function_16_1198(): pass

    label("Function_16_1198")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -50, 84460, 0)
    SetChrPos(0x101, 500, -50, 83960, 180)
    SetChrPos(0x102, -500, -50, 83960, 180)
    SetChrPos(0xF8, 500, -50, 84960, 180)
    SetChrPos(0xF9, -500, -50, 84960, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 19)
    Call(0, 20)
    Fade(500)
    OP_6D(80, 260, 81830, 0)
    SetChrPos(0x0, 80, 260, 81830, 180)
    SetChrPos(0x1, 80, 260, 81830, 180)
    SetChrPos(0x2, 80, 260, 81830, 180)
    SetChrPos(0x3, 80, 260, 81830, 180)
    EventEnd(0x0)
    Return()

    # Function_16_1198 end

    def Function_17_1293(): pass

    label("Function_17_1293")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -500, -50, 84960, 0)
    SetChrPos(0x102, 500, -50, 84960, 0)
    SetChrPos(0xF8, -500, -50, 83960, 0)
    SetChrPos(0xF9, 500, -50, 83960, 0)
    OP_0D()
    Call(0, 19)
    Call(0, 21)
    NewScene("ED6_DT21/C0701   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1293 end

    def Function_18_12F1(): pass

    label("Function_18_12F1")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_18_12F1 end

    def Function_19_13D0(): pass

    label("Function_19_13D0")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_19_13D0 end

    def Function_20_14AF(): pass

    label("Function_20_14AF")


    def lambda_14B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_14B5)

    def lambda_14C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_14C7)

    def lambda_14D9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_14D9)

    def lambda_14EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_14EB)
    Sleep(2500)
    Return()

    # Function_20_14AF end

    def Function_21_14FD(): pass

    label("Function_21_14FD")


    def lambda_1503():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1503)

    def lambda_1515():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1515)

    def lambda_1527():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1527)

    def lambda_1539():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1539)
    Sleep(2000)
    Return()

    # Function_21_14FD end

    SaveToFile()

Try(main)
