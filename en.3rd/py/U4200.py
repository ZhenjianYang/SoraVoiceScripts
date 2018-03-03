from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4200   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Armored Soldier',                      # 9
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
        'ED6_DT29/CH14510 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT29/CH14510P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 35780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5190,
        Y                   = -1000,
        Z                   = 32000,
        Range               = 4870,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8732,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 7050,
        TriggerZ            = 0,
        TriggerY            = 11870,
        TriggerRange        = 1000,
        ActorX              = 8000,
        ActorZ              = 3000,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_18F",          # 01, 1
        "Function_2_1D9",          # 02, 2
        "Function_3_356",          # 03, 3
        "Function_4_590",          # 04, 4
        "Function_5_B71",          # 05, 5
        "Function_6_BCA",          # 06, 6
        "Function_7_DA3",          # 07, 7
        "Function_8_E59",          # 08, 8
        "Function_9_F04",          # 09, 9
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_131")

    label("loc_126")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_149"),
        (SWITCH_DEFAULT, "loc_165"),
    )


    label("loc_149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_162")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_162")

    Jump("loc_165")

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_17B")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_18E")

    label("loc_17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_18E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_18E")

    Return()

    # Function_0_116 end

    def Function_1_18F(): pass

    label("Function_1_18F")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    OP_22(0x1CC, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_1B9")
    OP_B1("U4200_y")
    Jump("loc_1C2")

    label("loc_1B9")

    OP_B1("U4200_n")

    label("loc_1C2")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1D5")
    OP_82(0x81, 0x0)
    Jump("loc_1D8")

    label("loc_1D5")

    OP_82(0x82, 0x0)

    label("loc_1D8")

    Return()

    # Function_1_18F end

    def Function_2_1D9(): pass

    label("Function_2_1D9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_340")

    label("loc_1FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_340")

    label("loc_217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_340")

    label("loc_230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_340")

    label("loc_249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_340")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_340")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_340")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_340")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_340")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_340")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_340")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_340")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_340")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_355")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_340")

    label("loc_355")

    Return()

    # Function_2_1D9 end

    def Function_3_356(): pass

    label("Function_3_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_END)), "loc_35E")
    Return()

    label("loc_35E")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05A large armored soldier is blocking the path to the castle.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #1
        "\x07\x05Attempt to defeat it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_431"),
        (SWITCH_DEFAULT, "loc_500"),
    )


    label("loc_431")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_45C"),
        (2, "loc_46B"),
        (1, "loc_4EE"),
        (SWITCH_DEFAULT, "loc_4F3"),
    )


    label("loc_45C")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4F3")

    label("loc_46B")

    EventBegin(0x1)
    SetChrPos(0x0, 0, 0, 30130, 180)
    SetChrPos(0x1, 0, 0, 30130, 180)
    SetChrPos(0x2, 0, 0, 30130, 180)
    SetChrPos(0x3, 0, 0, 30130, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_4F3")

    label("loc_4EE")

    OP_B4(0x0)
    Jump("loc_4F3")

    label("loc_4F3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58C")

    label("loc_500")

    Sleep(300)
    Fade(500)
    SetChrPos(0x0, 0, 0, 30130, 180)
    SetChrPos(0x1, 0, 0, 30130, 180)
    SetChrPos(0x2, 0, 0, 30130, 180)
    SetChrPos(0x3, 0, 0, 30130, 180)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    EventEnd(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58C")

    label("loc_58C")

    Jump("loc_3EF")

    label("loc_58F")

    Return()

    # Function_3_356 end

    def Function_4_590(): pass

    label("Function_4_590")

    EventBegin(0x0)
    SetChrPos(0x10E, 0, 0, 28790, 0)
    SetChrPos(0x109, -950, 0, 27120, 0)
    SetChrPos(0x10F, 830, 0, 26490, 0)
    SetChrPos(0x107, -160, 0, 24800, 0)
    SetChrFlags(0x10, 0x80)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_6D(0, 5750, 42120, 0)
    OP_67(0, 4100, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_650():
        OP_6D(0, 4600, 36000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_650)

    def lambda_668():
        OP_67(0, 3200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_668)

    def lambda_680():
        OP_6B(3300, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_680)

    def lambda_690():
        OP_6E(343, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_690)

    def lambda_6A0():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x9B3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_6A0)
    Sleep(100)

    def lambda_6C0():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0x93EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C0)
    Sleep(100)

    def lambda_6E0():
        OP_8E(0xFE, 0x3B6, 0x0, 0x918C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6E0)
    Sleep(100)

    def lambda_700():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0x8C00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_700)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(2350, 600, 43360, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrPos(0x10E, -30, 0, 40240, 0)
    SetChrPos(0x109, -1110, 0, 38370, 0)
    SetChrPos(0x10F, 780, 0, 38590, 0)
    SetChrPos(0x107, -380, 0, 37000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x10E,
        "#178F#5PNo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#065F#4PWh-What's this magical symbol for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10F,
        (
            "#1443FI believe it's locked by a spiritual power of some\x01",
            "kind.\x02\x03",

            "We're unlikely to be able to force our way through\x01",
            "as long as it remains active, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10E,
        (
            "#176F#5PThat's certainly how it seems.\x02\x03",

            "#175FWhich means that we're going to need to find\x01",
            "some way to remove it, or we won't be able to\x01",
            "get inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1065F#6PMost likely, yeah.\x02\x03",

            "#1063FYou all right with us leaving the castle\x01",
            "until later, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 180, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10E,
        (
            "#178F#5PI fear we have little choice... I can only hope\x01",
            "that Aidios keeps everyone inside safe until\x01",
            "we can return.\x02\x03",

            "Shall we resume our search of the city in the\x01",
            "meantime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1060F#6PThat works.\x02\x03",

            "Hopefully, we can find some way of getting\x01",
            "inside while we're making the rounds.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(30, 0, 38110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x10E, 30, 0, 38110, 180)
    SetChrPos(0x109, 30, 0, 38110, 180)
    SetChrPos(0x10F, 30, 0, 38110, 180)
    SetChrPos(0x107, 30, 0, 38110, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x2704)
    OP_28(0x2B, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_4_590 end

    def Function_5_B71(): pass

    label("Function_5_B71")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_5_B71 end

    def Function_6_BCA(): pass

    label("Function_6_BCA")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA0")
    OP_28(0xD, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_CA0")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05#40WBring to me the guardian of the royal family\x01",
            "and the blade that serves the Imperial house.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D97")
    Call(0, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D94")
    Call(0, 7)

    label("loc_D94")

    Jump("loc_D97")

    label("loc_D97")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_6_BCA end

    def Function_7_DA3(): pass

    label("Function_7_DA3")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)

    def lambda_E0C():
        OP_6B(2830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E0C)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x0, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_DA3 end

    def Function_8_E59(): pass

    label("Function_8_E59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_8_E59 end

    def Function_9_F04(): pass

    label("Function_9_F04")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4203   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_9_F04 end

    SaveToFile()

Try(main)
