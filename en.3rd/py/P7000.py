from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P7000   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60211",
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


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 250,
        TriggerY            = 8380,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1250,
        ActorY              = 8380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5940,
        TriggerZ            = 250,
        TriggerY            = 13900,
        TriggerRange        = 800,
        ActorX              = -5940,
        ActorZ              = 1250,
        ActorY              = 13900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15830,
        TriggerZ            = 0,
        TriggerY            = 15070,
        TriggerRange        = 1600,
        ActorX              = 15830,
        ActorZ              = 1000,
        ActorY              = 15070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_223",          # 02, 2
        "Function_3_22F",          # 03, 3
        "Function_4_1442",         # 04, 4
        "Function_5_2E05",         # 05, 5
        "Function_6_3095",         # 06, 6
        "Function_7_3659",         # 07, 7
        "Function_8_39CD",         # 08, 8
        "Function_9_4D29",         # 09, 9
        "Function_10_4D3E",        # 0A, 10
        "Function_11_4D53",        # 0B, 11
        "Function_12_4D7C",        # 0C, 12
        "Function_13_4DA5",        # 0D, 13
        "Function_14_5E44",        # 0E, 14
        "Function_15_5F9D",        # 0F, 15
        "Function_16_5FDD",        # 10, 16
        "Function_17_601D",        # 11, 17
        "Function_18_605D",        # 12, 18
        "Function_19_609D",        # 13, 19
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_135")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_153")

    label("loc_135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_153")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F")
    Event(0, 8)

    label("loc_18F")

    Return()

    # Function_0_116 end

    def Function_1_190(): pass

    label("Function_1_190")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDFC60, 0x23007C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB")

    OP_1B(0x0, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_1D9")
    OP_64(0x0, 0x1)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x2)
    Jump("loc_1DF")

    label("loc_1D9")

    OP_72(0x1000, 0x0)
    ExitThread()

    label("loc_1DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F8")
    OP_64(0x1, 0x1)
    OP_71(0x1003, 0x0)
    ExitThread()
    Jump("loc_1FE")

    label("loc_1F8")

    OP_72(0x1003, 0x0)
    ExitThread()

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 6)), scpexpr(EXPR_END)), "loc_215")
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 15)
    Jump("loc_222")

    label("loc_215")

    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)

    label("loc_222")

    Return()

    # Function_1_190 end

    def Function_2_223(): pass

    label("Function_2_223")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_2_223 end

    def Function_3_22F(): pass

    label("Function_3_22F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(500, -250, -38000, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(44000, 0)
    OP_6E(304, 0)
    SetChrPos(0x109, -680, -250, -37490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    SetChrPos(0xEF, 700, -250, -37780, 0)
    SetChrPos(0xF0, -640, -250, -39170, 0)
    SetChrPos(0xF1, 960, -250, -39410, 0)
    Jump("loc_352")

    label("loc_2CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    SetChrPos(0xF0, 700, -250, -37780, 0)
    SetChrPos(0xEF, -640, -250, -39170, 0)
    SetChrPos(0xF1, 960, -250, -39410, 0)
    Jump("loc_352")

    label("loc_311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352")
    SetChrPos(0xF1, 700, -250, -37780, 0)
    SetChrPos(0xEF, -640, -250, -39170, 0)
    SetChrPos(0xF0, 960, -250, -39410, 0)

    label("loc_352")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_393():
        OP_6D(800, -250, -29760, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_393)

    def lambda_3AB():
        OP_67(0, 6800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_3AB)

    def lambda_3C3():
        OP_6B(2660, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_3C3)

    def lambda_3D3():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_3D3)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3ED():
        OP_8E(0xFE, 0xFFFFFC90, 0xFFFFFF06, 0xFFFF8A1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3ED)

    def lambda_408():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_408)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")

    def lambda_42D():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_42D)

    def lambda_448():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_448)
    Sleep(100)

    def lambda_45F():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_45F)

    def lambda_47A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_47A)
    Sleep(100)

    def lambda_491():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_491)

    def lambda_4AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4AC)
    Jump("loc_5FC")

    label("loc_4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")

    def lambda_4CF():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_4CF)

    def lambda_4EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4EA)
    Sleep(100)

    def lambda_501():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_501)

    def lambda_51C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_51C)
    Sleep(100)

    def lambda_533():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_533)

    def lambda_54E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_54E)
    Jump("loc_5FC")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FC")

    def lambda_571():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_571)

    def lambda_58C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_58C)
    Sleep(100)

    def lambda_5A3():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5A3)

    def lambda_5BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5BE)
    Sleep(100)

    def lambda_5D5():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5D5)

    def lambda_5F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_5F0)

    label("loc_5FC")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x2)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#11PWhere...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1065F#5P...I knew it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AF")
    OP_A2(0x0)

    ChrTalk(    #2
        0x101,
        (
            "#1004F#6PWhere are we now?\x02\x03",

            "This doesn't look like Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_6AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_715")
    OP_A2(0x2)

    ChrTalk(    #3
        0x102,
        (
            "#1502F#6PWhere are we now?\x02\x03",

            "It doesn't look like Erbe Royal Villa, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")
    OP_A2(0x5)

    ChrTalk(    #4
        0x110,
        (
            "#1306F#6POh?\x02\x03",

            "It's like we've ended up somewhere different\x01",
            "entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D2")
    OP_A2(0x1)

    ChrTalk(    #5
        0x107,
        (
            "#065F#6PWhere are we now?\x02\x03",

            "This doesn't look like Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84F")
    OP_A2(0x3)

    ChrTalk(    #6
        0x10A,
        (
            "#814F#6PHuh? Where are we now?\x02\x03",

            "I don't remember the front of Erbe Royal Villa\x01",
            "looking like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_84F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89E")

    ChrTalk(    #7
        0x105,
        (
            "#1162F#6PWhere are we now?\x02\x03",

            "This isn't Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_89E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FB")

    ChrTalk(    #8
        0x103,
        (
            "#1522F#6PWhere are we now?\x02\x03",

            "This doesn't look like Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_8FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_966")

    ChrTalk(    #9
        0x106,
        (
            "#555F#6PWhere are we now?\x02\x03",

            "This doesn't look like the royal villa as \x01",
            "I remember it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_966")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2")

    ChrTalk(    #10
        0x108,
        (
            "#072F#6PWhere are we now?\x02\x03",

            "This doesn't look like Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_9C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(    #11
        0x10E,
        (
            "#178F#6PWhere are we now?\x02\x03",

            "This isn't Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_A10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7C")

    ChrTalk(    #12
        0x104,
        (
            "#1542F#6PWhere are we now?\x02\x03",

            "This doesn't look like the royal villa as \x01",
            "I remember it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(    #13
        0x10C,
        (
            "#112F#6PWhere are we now?\x02\x03",

            "This doesn't look like Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B55")
    OP_A2(0x4)

    ChrTalk(    #14
        0x10B,
        (
            "#216F#6PWh-Where are we now?\x02\x03",

            "This doesn't seem like somewhere attached\x01",
            "to the road we were just on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B93")

    ChrTalk(    #15
        0x109,
        "#1840F#5POh, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB3")

    label("loc_B93")


    ChrTalk(    #16
        0x109,
        "#1840F#5POh, you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_BB3")

    OP_1D(0xB2)

    def lambda_BBB():
        OP_6D(0, 8000, -26000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_BBB)

    def lambda_BD3():
        OP_67(0, 3800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_BD3)

    def lambda_BEB():
        OP_6B(2670, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_BEB)

    def lambda_BFB():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BFB)

    def lambda_C0B():
        OP_6E(335, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_C0B)
    Sleep(1000)

    def lambda_C20():
        OP_8F(0xFE, 0x0, 0xFFFFFF06, 0xFFFF9DC2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C20)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0x109, 0x0)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    SetChrPos(0xEF, 780, -250, -29300, 0)
    SetChrPos(0xF0, -650, -250, -31120, 0)
    SetChrPos(0xF1, 1260, -250, -31070, 0)
    Jump("loc_D14")

    label("loc_C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD3")
    SetChrPos(0xF0, 780, -250, -29300, 0)
    SetChrPos(0xEF, -650, -250, -31120, 0)
    SetChrPos(0xF1, 1260, -250, -31070, 0)
    Jump("loc_D14")

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D14")
    SetChrPos(0xF1, 780, -250, -29300, 0)
    SetChrPos(0xEF, -650, -250, -31120, 0)
    SetChrPos(0xF0, 1260, -250, -31070, 0)

    label("loc_D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    Jump("loc_D44")

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D36")
    Jump("loc_D44")

    label("loc_D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")

    label("loc_D44")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D90")

    ChrTalk(    #17
        0x10D,
        "#273F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_D90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD7")

    ChrTalk(    #18
        0x10B,
        "#213F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1E")

    ChrTalk(    #19
        0x10C,
        "#113F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E66")

    ChrTalk(    #20
        0x104,
        "#1543F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_E66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAD")

    ChrTalk(    #21
        0x10E,
        "#173F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF4")

    ChrTalk(    #22
        0x108,
        "#073F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3B")

    ChrTalk(    #23
        0x106,
        "#052F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_F3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(    #24
        0x103,
        "#1523F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_F83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCB")

    ChrTalk(    #25
        0x105,
        "#1164F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1012")

    ChrTalk(    #26
        0x10A,
        "#814F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_1012")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1059")

    ChrTalk(    #27
        0x107,
        "#064F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_1059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A0")

    ChrTalk(    #28
        0x110,
        "#264F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_10A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E8")

    ChrTalk(    #29
        0x102,
        "#1504F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_10E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112D")

    ChrTalk(    #30
        0x101,
        "#1004F#5PWait... Isn't that the church's emblem?!\x02",
    )

    CloseMessageWindow()

    label("loc_112D")


    ChrTalk(    #31
        0x10F,
        "#1802F#5PKevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_115C():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFA434, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_115C)
    Sleep(500)
    Fade(1000)
    OP_6D(0, 600, -23500, 0)
    OP_67(0, 3160, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(345, 0)

    def lambda_11BE():
        OP_6D(0, 300, -23500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_11BE)

    def lambda_11D6():
        OP_67(0, 3220, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_11D6)

    def lambda_11EE():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_11EE)

    def lambda_11FE():
        OP_6E(312, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11FE)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    OP_22(0x176, 0x0, 0x64)
    OP_B0(0x4, 0x5)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)
    WaitChrThread(0xEE, 0x1)
    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12FE")

    ChrTalk(    #33
        0x109,
        (
            "#1075F#5PWelcome to Aster House.\x02\x03",

            "#1840FThe place where Ries, Rufina, and I grew up\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_12FE")


    ChrTalk(    #34
        0x109,
        (
            "#1075F#5PWelcome to Aster House.\x02\x03",

            "#1840FThe place where Ries, Rufina, and I grew up\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")


    def lambda_1367():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1367)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    Sleep(2000)
    OP_A2(0x2B2E)
    OP_AD(0x2400F2, 0x0, 0x0, 0x64)
    OP_F7(0x6, 0x0, 0x0)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F9")
    ShowSaveMenu()

    label("loc_13F9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_22F end

    def Function_4_1442(): pass

    label("Function_4_1442")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_AD(0x2400E9, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -320, -250, -22480, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    SetChrPos(0xEF, -600, -250, -25060, 0)
    SetChrPos(0xF0, -1000, -250, -27000, 0)
    SetChrPos(0xF1, 470, -250, -27430, 0)
    Jump("loc_162B")

    label("loc_15A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EA")
    SetChrPos(0xF0, -600, -250, -25060, 0)
    SetChrPos(0xEF, -1000, -250, -27000, 0)
    SetChrPos(0xF1, 470, -250, -27430, 0)
    Jump("loc_162B")

    label("loc_15EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162B")
    SetChrPos(0xF1, -600, -250, -25060, 0)
    SetChrPos(0xEF, -1000, -250, -27000, 0)
    SetChrPos(0xF0, 470, -250, -27430, 0)

    label("loc_162B")

    OP_6D(-2170, -450, -17930, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(315000, 0)
    OP_6E(422, 0)
    OP_1D(0xD3)

    def lambda_1670():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1670)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F6")

    def lambda_169E():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_169E)
    Sleep(100)

    def lambda_16BE():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_16BE)
    Sleep(100)

    def lambda_16DE():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_16DE)
    Jump("loc_17CB")

    label("loc_16F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1762")

    def lambda_170A():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_170A)
    Sleep(100)

    def lambda_172A():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_172A)
    Sleep(100)

    def lambda_174A():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_174A)
    Jump("loc_17CB")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CB")

    def lambda_1776():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1776)
    Sleep(100)

    def lambda_1796():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1796)
    Sleep(100)

    def lambda_17B6():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_17B6)

    label("loc_17CB")


    def lambda_17D1():
        OP_6B(3400, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_17D1)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-14220, 150, 2220, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(315000, 0)
    OP_6E(439, 0)

    def lambda_1836():
        OP_6D(-14220, 150, -3430, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1836)

    def lambda_184E():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_184E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C5")

    def lambda_1877():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1877)

    def lambda_1892():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1892)

    def lambda_18AD():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_18AD)
    Jump("loc_1986")

    label("loc_18C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1927")

    def lambda_18D9():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_18D9)

    def lambda_18F4():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_18F4)

    def lambda_190F():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_190F)
    Jump("loc_1986")

    label("loc_1927")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1986")

    def lambda_193B():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_193B)

    def lambda_1956():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1956)

    def lambda_1971():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1971)

    label("loc_1986")

    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(11330, -1100, 5620, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(315000, 0)
    OP_6E(400, 0)

    def lambda_19D8():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_19D8)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-3520, -250, 15320, 0)
    OP_67(0, 8220, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(315000, 0)
    OP_6E(398, 0)

    def lambda_1A34():
        OP_6D(-3070, -250, 6170, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1A34)

    def lambda_1A4C():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A4C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC3")

    def lambda_1A75():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1A75)

    def lambda_1A90():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1A90)

    def lambda_1AAB():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1AAB)
    Jump("loc_1B84")

    label("loc_1AC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B25")

    def lambda_1AD7():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1AD7)

    def lambda_1AF2():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1AF2)

    def lambda_1B0D():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B0D)
    Jump("loc_1B84")

    label("loc_1B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B84")

    def lambda_1B39():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B39)

    def lambda_1B54():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B54)

    def lambda_1B6F():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1B6F)

    label("loc_1B84")

    OP_C8(0x80, 0x46, "C_PLAC36._CH", 0x1, 0x3E8)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-1600, -250, 3200, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #35
        0x10F,
        (
            "#1802F#6PThis is...only a copy of Aster House, yes?\x02\x03",

            "B-But it looks so...so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1065F#5PYeah. I can barely bring myself to accept it's\x01",
            "not the real thing.\x02\x03",

            "#1840FEverything from the feel of the earth underfoot\x01",
            "to the smells in the air are just like the real\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1445F#6PYeah...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(    #38
        0x110,
        "#1300F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_1D4D")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #39
        0x103,
        (
            "#1522F#6PThis is where the two of you grew up?\x02\x03",

            "Judging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_1E09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB3")

    ChrTalk(    #40
        0x105,
        (
            "#1163F#6PThis is where the two of you grew up?\x02\x03",

            "Judging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F47")
    OP_A2(0x0)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#6PSo this is where the two of you grew up, huh?\x02\x03",

            "I'm guessing this is somewhere owned by the\x01",
            "Septian Church, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_1F47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFF")
    OP_A2(0x2)

    ChrTalk(    #42
        0x102,
        (
            "#1505F#6PSo this is where the two of you grew up...\x02\x03",

            "#1502FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2092")
    OP_A2(0x3)

    ChrTalk(    #43
        0x10A,
        (
            "#812F#6PSo this is where the two of you grew up, huh?\x02\x03",

            "I'm guessing this is somewhere owned by the\x01",
            "Septian Church, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_2092")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(    #44
        0x106,
        (
            "#053F#6PSo this is where the two of you grew up, huh?\x02\x03",

            "#050FSo I'm guessing this is some kind of place owned\x01",
            "by the Septian Church, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_2133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E9")

    ChrTalk(    #45
        0x108,
        (
            "#074F#6PSo this is where the two of you grew up, huh?\x02\x03",

            "#072FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_21E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229A")

    ChrTalk(    #46
        0x10E,
        (
            "#176F#6PSo this is where the two of you grew up?\x02\x03",

            "#178FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_229A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234D")

    ChrTalk(    #47
        0x104,
        (
            "#1545F#6PSo this is where the two of you grew up?\x02\x03",

            "#1540FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_234D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FE")

    ChrTalk(    #48
        0x10D,
        (
            "#272F#6PSo this is where the two of you grew up?\x02\x03",

            "#270FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_23FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AF")

    ChrTalk(    #49
        0x10C,
        (
            "#115F#6PSo this is where the two of you grew up?\x02\x03",

            "#112FJudging by the emblem at the entrance, I take it\x01",
            "this is a facility operated by the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_24AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2505")
    OP_A2(0x1)

    ChrTalk(    #50
        0x107,
        (
            "#062F#6PUmm...\x02\x03",

            "So is this Aster House a church-owned place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2558")

    label("loc_2505")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2558")
    OP_A2(0x4)

    ChrTalk(    #51
        0x10B,
        (
            "#212F#6PUmm...\x02\x03",

            "So is this Aster House a church-owned place?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25FA")

    ChrTalk(    #52
        0x109,
        (
            "#1075F#5PThat's right. It's what's called a gospel facility.\x02\x03",

            "#1840FThink of them as a cross between an orphanage\x01",
            "and a monastery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2682")

    label("loc_25FA")


    ChrTalk(    #53
        0x109,
        (
            "#1075F#5PThat's right. It's what's called a gospel facility.\x02\x03",

            "#1840FThink of them as a cross between an orphanage\x01",
            "and a monastery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2682")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(    #54
        0x103,
        (
            "#1525F#6PI see...\x02\x03",

            "#1532F...\x02\x03",

            "#1534FThen...you're an orphan, too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_26EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2738")

    ChrTalk(    #55
        0x105,
        (
            "#1169F#6PI see...\x02\x03",

            "#1382FSo that means you must be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2780")
    OP_A2(0x0)

    ChrTalk(    #56
        0x101,
        (
            "#1003F#6PI see...\x02\x03",

            "#1025FSo does that mean...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27CA")
    OP_A2(0x2)

    ChrTalk(    #57
        0x102,
        (
            "#1503F#6PI see...\x02\x03",

            "#1500FSo that means you're...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_27CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2813")
    OP_A2(0x3)

    ChrTalk(    #58
        0x10A,
        (
            "#1316F#6PI see...\x02\x03",

            "#810FSo that means you're...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2858")

    ChrTalk(    #59
        0x106,
        (
            "#551F#6PRight...\x02\x03",

            "#555FSo that means you're...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_289D")

    ChrTalk(    #60
        0x108,
        (
            "#572F#6PI see...\x02\x03",

            "#070FSo that means you're...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_289D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E8")

    ChrTalk(    #61
        0x10E,
        (
            "#175F#6PI see...\x02\x03",

            "#170FSo that means that you are...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_28E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(    #62
        0x104,
        (
            "#1540F#6PHmm... I see.\x02\x03",

            "So am I right in assuming that you must be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2998")

    ChrTalk(    #63
        0x10D,
        (
            "#270F#6PI see.\x02\x03",

            "So am I right in assuming that you must be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E0")

    ChrTalk(    #64
        0x10C,
        (
            "#110F#6PI see...\x02\x03",

            "But then that would make you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_29E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A33")
    OP_A2(0x1)

    ChrTalk(    #65
        0x107,
        (
            "#561F#6PO-Oh, right...\x02\x03",

            "#560FSo does that mean you're...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7F")

    label("loc_2A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7F")
    OP_A2(0x4)

    ChrTalk(    #66
        0x10B,
        (
            "#215F#6POh, right.\x02\x03",

            "#210FSo does that mean you're...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B7A")

    ChrTalk(    #67
        0x109,
        (
            "#1075F#5PWell, no reason to dance around it, so yep.\x01",
            "I'm an orphan.\x02\x03",

            "#1840FAnd how I came to be here is a story best\x01",
            "saved for another day.\x02\x03",

            "#1067FFeels weird being back here again, though...\x01",
            "It's been about five years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5B")

    label("loc_2B7A")


    ChrTalk(    #68
        0x109,
        (
            "#1075F#5PWell, no reason to dance around it, so yep.\x01",
            "I'm an orphan.\x02\x03",

            "#1840FAnd how I came to be here is a story best\x01",
            "saved for another day.\x02\x03",

            "#1067FFeels weird being back here again, though...\x01",
            "It's been about five years.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5B")


    ChrTalk(    #69
        0x10F,
        "#1445F#6PFive very long years...\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)

    def lambda_2CA1():
        OP_6D(-1600, -250, 2000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2CA1)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x0, 0x1)
    Sleep(300)

    ChrTalk(    #70
        0x109,
        (
            "#1078F#11PWell, anyway. We're bound to find some kind\x01",
            "of clue as to how to get to the seventh plane\x01",
            "somewhere in here.\x02\x03",

            "You guys up for having a look around the area\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        "#1806F#6PYeah. Let's go.\x02",
    )

    CloseMessageWindow()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A2(0x2C00)
    OP_28(0x37, 0x4, 0x10)
    OP_28(0x37, 0x4, 0x20)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x4, 0x20)
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3B, 0x4, 0x20)
    OP_28(0x3C, 0x4, 0x4)
    OP_28(0x3C, 0x4, 0x8)
    OP_28(0x3C, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_1442 end

    def Function_5_2E05(): pass

    label("Function_5_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 2)), scpexpr(EXPR_END)), "loc_2E14")
    Call(0, 13)
    Return()

    label("loc_2E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3040")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-520, 250, 7630, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3570, 0)
    OP_6C(315000, 0)
    OP_6E(225, 0)
    SetChrPos(0x109, 240, 250, 7560, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB5")
    SetChrPos(0xEF, 280, -250, 6090, 0)
    SetChrPos(0xF0, -190, -250, 4650, 0)
    SetChrPos(0xF1, 1320, -250, 4570, 0)
    Jump("loc_2F3A")

    label("loc_2EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF9")
    SetChrPos(0xF0, 280, -250, 6090, 0)
    SetChrPos(0xEF, -190, -250, 4650, 0)
    SetChrPos(0xF1, 1320, -250, 4570, 0)
    Jump("loc_2F3A")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3A")
    SetChrPos(0xF1, 280, -250, 6090, 0)
    SetChrPos(0xEF, -190, -250, 4650, 0)
    SetChrPos(0xF0, 1320, -250, 4570, 0)

    label("loc_2F3A")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #72
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #73
        0x109,
        "#1067F#5PFigures.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10F,
        "#1802F#6PIs it locked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        (
            "#1840F#5PYeah...\x02\x03",

            "#1065F...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #76
        0x109,
        "#1078F#11PWell, whatever. We can keep poking around.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C01)
    OP_28(0x3C, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_3094")

    label("loc_3040")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #77
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_3094")

    Return()

    # Function_5_2E05 end

    def Function_6_3095(): pass

    label("Function_6_3095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-6360, 250, 15270, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(248, 0)
    SetChrPos(0x109, -6690, 250, 13820, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3136")
    SetChrPos(0xEF, -8390, 250, 13620, 90)
    SetChrPos(0xF0, -9870, 250, 14040, 90)
    SetChrPos(0xF1, -9820, 250, 12750, 90)
    Jump("loc_31BB")

    label("loc_3136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_317A")
    SetChrPos(0xF0, -8390, 250, 13620, 90)
    SetChrPos(0xEF, -9870, 250, 14040, 90)
    SetChrPos(0xF1, -9820, 250, 12750, 90)
    Jump("loc_31BB")

    label("loc_317A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BB")
    SetChrPos(0xF1, -8390, 250, 13620, 90)
    SetChrPos(0xEF, -9870, 250, 14040, 90)
    SetChrPos(0xF0, -9820, 250, 12750, 90)

    label("loc_31BB")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #78
        "\x07\x05The door is stuck fast and doesn't have a keyhole.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326A")

    ChrTalk(    #79
        0x10C,
        "#112F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_326A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A1")

    ChrTalk(    #80
        0x10D,
        "#270F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_32A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D9")

    ChrTalk(    #81
        0x104,
        "#1543F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_32D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3310")

    ChrTalk(    #82
        0x10E,
        "#178F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_3310")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3347")

    ChrTalk(    #83
        0x108,
        "#073F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_3347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337E")

    ChrTalk(    #84
        0x106,
        "#555F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_337E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B9")

    ChrTalk(    #85
        0x10A,
        "#814F#6PHuh? How come it won't open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_33B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33DC")

    ChrTalk(    #86
        0x107,
        "#064F#6PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_33DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_340D")

    ChrTalk(    #87
        0x110,
        "#267F#6PWhy won't it open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_340D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3445")

    ChrTalk(    #88
        0x102,
        "#1504F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_3445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(    #89
        0x101,
        "#1004F#6PHmm? Won't it open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_3478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B0")

    ChrTalk(    #90
        0x103,
        "#1522F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_34B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E5")

    ChrTalk(    #91
        0x105,
        "#1164F#6PHow does this door open?\x02",
    )

    CloseMessageWindow()

    label("loc_34E5")


    def lambda_34EB():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_34EB)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #92
        0x10F,
        (
            "#1448F#11PThis is a side entrance that only opens from\x01",
            "the inside. We can't get in from the outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x109,
        (
            "#1840F#11PYeah. If we want to get into the chapel,\x01",
            "we're gonna have to go through the front.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C02)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_3658")

    label("loc_35DD")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #94
        "\x07\x05The door is sealed shut and doesn't have a keyhole.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_3658")

    Return()

    # Function_6_3095 end

    def Function_7_3659(): pass

    label("Function_7_3659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3989")
    EventBegin(0x0)
    Fade(500)
    OP_6D(15000, 0, 15010, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(0, 0)
    OP_6E(221, 0)
    SetChrPos(0x109, 14490, 0, 13580, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36FA")
    SetChrPos(0xEF, 15370, 0, 12430, 0)
    SetChrPos(0xF0, 13290, 0, 12680, 45)
    SetChrPos(0xF1, 14210, 0, 11570, 45)
    Jump("loc_377F")

    label("loc_36FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373E")
    SetChrPos(0xF0, 15370, 0, 12430, 0)
    SetChrPos(0xEF, 13290, 0, 12680, 45)
    SetChrPos(0xF1, 14210, 0, 11570, 45)
    Jump("loc_377F")

    label("loc_373E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377F")
    SetChrPos(0xF1, 15370, 0, 12430, 0)
    SetChrPos(0xEF, 13290, 0, 12680, 45)
    SetChrPos(0xF0, 14210, 0, 11570, 45)

    label("loc_377F")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #95
        "\x07\x05There's an empty well.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #96
        0x109,
        (
            "#1060F#5PWe used to get our drinking water out of here.\x02\x03",

            "#1068FWe had no fancy orbal pumps, either. We did it\x01",
            "all using a good, old-fashioned bucket with string\x01",
            "attached... It was a nightmare!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10F,
        (
            "#1446F#6PTell me about it...\x02\x03",

            "We would go out on winter mornings and come\x01",
            "back with our hands numb and red raw.\x02\x03",

            "#1806FBut looking back on the whole experience now,\x01",
            "it was fun in its own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x109,
        "#1066F#5PHaha. I guess it was.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C03)
    OP_28(0x3C, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_39CC")

    label("loc_3989")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #99
        "\x07\x05There's an empty well.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_39CC")

    Return()

    # Function_7_3659 end

    def Function_8_39CD(): pass

    label("Function_8_39CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13380, 250, -9700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2E")
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF0, -13380, 250, -9700, 90)
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    Jump("loc_3AB3")

    label("loc_3A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A72")
    SetChrPos(0xF0, -13380, 250, -9700, 90)
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    Jump("loc_3AB3")

    label("loc_3A72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB3")
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF0, -13380, 250, -9700, 90)

    label("loc_3AB3")

    OP_6D(-12370, 250, -8380, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(314000, 0)
    OP_6E(245, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    OP_73(0x1)
    Sleep(300)

    def lambda_3B21():
        OP_6D(-7600, -250, -8460, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3B21)

    def lambda_3B39():
        OP_67(0, 5330, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3B39)
    OP_43(0x109, 0x0, 0x0, 0x9)
    Sleep(700)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B87")
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    Jump("loc_3BE4")

    label("loc_3B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB7")
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    Jump("loc_3BE4")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE4")
    OP_43(0xF1, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xC)

    label("loc_3BE4")

    Sleep(1000)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1001, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #100
        0x10F,
        (
            "#1445F#5PThere was no sign of anything in there.\x02\x03",

            "#1443FOur last hope seems to be the chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1067F#5PSo it seems...\x02\x03",

            "#1065F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #102
        0x10F,
        "#1802F#5PWhat is it, Kevin?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #103
        0x109,
        (
            "#1840F#6P...Hey, Ries?\x02\x03",

            "You were the one responsible for cleaning\x01",
            "the chapel that day, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10F,
        "#1444F#5PWhat day...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x109,
        (
            "#1067F#6POn Aster House's final day.\x02\x03",

            "#1065FWhen Rufina died.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD9")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E40")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E01")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E40")

    label("loc_3E01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E29")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E40")

    label("loc_3E29")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E40")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3ED4")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E95")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3ED4")

    label("loc_3E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EBD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3ED4")

    label("loc_3EBD")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3ED4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F01")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F68")

    label("loc_3F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F29")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F68")

    label("loc_3F29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F51")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F68")

    label("loc_3F51")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3F68")

    Sleep(1000)

    ChrTalk(    #106
        0x10F,
        "#1445F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA7")

    ChrTalk(    #107
        0x101,
        "#1020F#5PK-Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_401B")

    label("loc_3FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCE")

    ChrTalk(    #108
        0x107,
        "#065F#5PK-Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_401B")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF6")

    ChrTalk(    #109
        0x10A,
        "#1317F#5PK-Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_401B")

    label("loc_3FF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401B")

    ChrTalk(    #110
        0x105,
        "#1163F#5PK-Kevin?\x02",
    )

    CloseMessageWindow()

    label("loc_401B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_403F")

    ChrTalk(    #111
        0x110,
        "#1305F#5POho?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4089")

    label("loc_403F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4065")

    ChrTalk(    #112
        0x10C,
        "#112F#5PHmm...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4089")

    label("loc_4065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4089")

    ChrTalk(    #113
        0x104,
        "#1542F#5PHmm...?\x02",
    )

    CloseMessageWindow()

    label("loc_4089")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B9")

    ChrTalk(    #114
        0x102,
        "#1502F#5PYou don't think...?\x02",
    )

    CloseMessageWindow()

    label("loc_40B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E3")

    ChrTalk(    #115
        0x10B,
        "#212F#5PWh-What...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_40E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_410B")

    ChrTalk(    #116
        0x103,
        "#1522F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_410B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4132")

    ChrTalk(    #117
        0x106,
        "#057F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_4132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4159")

    ChrTalk(    #118
        0x108,
        "#072F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_4159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4180")

    ChrTalk(    #119
        0x10E,
        "#178F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_4180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A4")

    ChrTalk(    #120
        0x10D,
        "#270F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    label("loc_41A4")


    ChrTalk(    #121
        0x109,
        (
            "#1063F#6PThat was what I was told when I went to visit\x01",
            "the matron afterward, at least.\x02\x03",

            "Well? Were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10F,
        (
            "#1445F#5PY-Yeah...\x02\x03",

            "#1802FI was. Why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1075F#6PI thought so.\x02\x03",

            "#1840FCheck your pockets, Ries.\x02\x03",

            "I'm pretty sure the chapel key's in one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10F,
        "#1444F#5PHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #125
        (
            "\x07\x05Ries began checking the pockets of her habit.\x02\x03",

            "\x07\x05Eventually, she found an old brass key.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x05Found \x1F\x38\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x338, 1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43AA")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4411")

    label("loc_43AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D2")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4411")

    label("loc_43D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43FA")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4411")

    label("loc_43FA")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4411")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443E")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_44A5")

    label("loc_443E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4466")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_44A5")

    label("loc_4466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_44A5")

    label("loc_448E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_44A5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D2")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4539")

    label("loc_44D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44FA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4539")

    label("loc_44FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4522")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4539")

    label("loc_4522")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4539")

    Sleep(1000)

    ChrTalk(    #127
        0x10F,
        "#1802F#5PIt can't be...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4581")

    ChrTalk(    #128
        0x101,
        "#1004F#5PN-No way!\x02",
    )

    CloseMessageWindow()

    label("loc_4581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B1")

    ChrTalk(    #129
        0x105,
        "#1164F#5PIs that the key...?\x02",
    )

    CloseMessageWindow()

    label("loc_45B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45D9")

    ChrTalk(    #130
        0x10B,
        "#216F#5PS-Seriously?\x02",
    )

    CloseMessageWindow()

    label("loc_45D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4620")

    ChrTalk(    #131
        0x106,
        "#055F#5PWow... There's a twist I didn't see coming.\x02",
    )

    CloseMessageWindow()

    label("loc_4620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4659")

    ChrTalk(    #132
        0x103,
        "#1525F#5PThat's quite the surprise...\x02",
    )

    CloseMessageWindow()

    label("loc_4659")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4684")

    ChrTalk(    #133
        0x10E,
        "#173F#5PUnbelievable...\x02",
    )

    CloseMessageWindow()

    label("loc_4684")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46BC")

    ChrTalk(    #134
        0x10A,
        "#814F#5PWh-What's that doing there?!\x02",
    )

    CloseMessageWindow()

    label("loc_46BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DE")

    ChrTalk(    #135
        0x10D,
        "#276F#5PHmm...\x02",
    )

    CloseMessageWindow()

    label("loc_46DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470E")

    ChrTalk(    #136
        0x108,
        "#074F#5PHaha... Interesting.\x02",
    )

    CloseMessageWindow()

    label("loc_470E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4851")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4744")

    ChrTalk(    #137
        0x10C,
        "#115F#5PI see now...\x02",
    )

    CloseMessageWindow()

    label("loc_4744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_476A")

    ChrTalk(    #138
        0x110,
        "#1306F#5POh, my...\x02",
    )

    CloseMessageWindow()

    label("loc_476A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478C")

    ChrTalk(    #139
        0x102,
        "#1504F#5PAh...\x02",
    )

    CloseMessageWindow()

    label("loc_478C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47BE")

    ChrTalk(    #140
        0x107,
        "#065F#5PHow'd that get there?!\x02",
    )

    CloseMessageWindow()

    label("loc_47BE")


    ChrTalk(    #141
        0x104,
        (
            "#1545F#5PThis is a surprise...\x02\x03",

            "#1540FI suppose this is just another manifestation\x01",
            "of this world's ability to make thoughts into \x01",
            "reality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5E")

    label("loc_4851")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4961")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4885")

    ChrTalk(    #142
        0x110,
        "#1306F#5POh, my...\x02",
    )

    CloseMessageWindow()

    label("loc_4885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48A7")

    ChrTalk(    #143
        0x102,
        "#1504F#5PAh...\x02",
    )

    CloseMessageWindow()

    label("loc_48A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48D9")

    ChrTalk(    #144
        0x107,
        "#065F#5PHow'd that get there?!\x02",
    )

    CloseMessageWindow()

    label("loc_48D9")


    ChrTalk(    #145
        0x10C,
        (
            "#115F#5PI see now...\x02\x03",

            "#112FI suppose this is just another manifestation\x01",
            "of this world's ability to make thoughts into \x01",
            "reality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5E")

    label("loc_4961")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4991")

    ChrTalk(    #146
        0x102,
        "#1504F#5PAh...\x02",
    )

    CloseMessageWindow()

    label("loc_4991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49C3")

    ChrTalk(    #147
        0x107,
        "#065F#5PHow'd that get there?!\x02",
    )

    CloseMessageWindow()

    label("loc_49C3")


    ChrTalk(    #148
        0x110,
        (
            "#263F#5PThat makes sense.\x02\x03",

            "#1306FThis is just another manifestation of this world's\x01",
            "ability to make thoughts into reality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5E")

    label("loc_4A46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ACD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A76")

    ChrTalk(    #149
        0x102,
        "#1504F#5PAh...\x02",
    )

    CloseMessageWindow()

    label("loc_4A76")


    ChrTalk(    #150
        0x107,
        (
            "#062F#5PW-Wait...\x02\x03",

            "Is this another case of this world making\x01",
            "thoughts reality?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5E")

    label("loc_4ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B5E")

    ChrTalk(    #151
        0x102,
        (
            "#1503F#5PI see now...\x02\x03",

            "#1502FI guess this is just another manifestation of\x01",
            "Phantasma's ability to make thoughts into\x01",
            "reality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5E")


    ChrTalk(    #152
        0x109,
        (
            "#1841F#6PHonestly, I wasn't entirely sure you'd\x01",
            "find it in there.\x02\x03",

            "#1840FBut in all the other areas on this plane,\x01",
            "there was always a reason to take the\x01",
            "person we needed with us.\x02\x03",

            "This just goes to show that you really\x01",
            "were meant to come here, Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10F,
        (
            "#1445F#5PBut... But...\x02\x03",

            "...\x02\x03",

            "#1443FNo... As disbelieving as I am, this is definitely\x01",
            "the chapel's key.\x02\x03",

            "I suppose all we can do right now is try to go\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x109,
        "#1067F#6P...Yeah.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C0A)
    OP_28(0x3C, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_8_39CD end

    def Function_9_4D29(): pass

    label("Function_9_4D29")

    OP_8F(0xFE, 0xFFFFEC64, 0xFFFFFF1A, 0xFFFFD9C2, 0x7D0, 0x0)
    Return()

    # Function_9_4D29 end

    def Function_10_4D3E(): pass

    label("Function_10_4D3E")

    OP_8F(0xFE, 0xFFFFE5DE, 0xFFFFFF06, 0xFFFFD9A4, 0x7D0, 0x0)
    Return()

    # Function_10_4D3E end

    def Function_11_4D53(): pass

    label("Function_11_4D53")

    OP_8F(0xFE, 0xFFFFD490, 0xFA, 0xFFFFDA12, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFE214, 0xFFFFFF06, 0xFFFFD6B6, 0x7D0, 0x0)
    Return()

    # Function_11_4D53 end

    def Function_12_4D7C(): pass

    label("Function_12_4D7C")

    OP_8F(0xFE, 0xFFFFD490, 0xFA, 0xFFFFDA12, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFE02A, 0xFFFFFF06, 0xFFFFDC74, 0x7D0, 0x0)
    Return()

    # Function_12_4D7C end

    def Function_13_4DA5(): pass

    label("Function_13_4DA5")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-800, 250, 7630, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(315000, 0)
    OP_6E(231, 0)
    OP_6D(-800, 250, 7630, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(315000, 0)
    OP_6E(231, 0)
    SetChrPos(0x109, 0, -250, 6090, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7B")
    SetChrPos(0xEF, 240, 250, 7560, 0)
    SetChrPos(0xF0, -470, -250, 4550, 0)
    SetChrPos(0xF1, 1040, -250, 4470, 0)
    Jump("loc_4F00")

    label("loc_4E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EBF")
    SetChrPos(0xF0, 240, 250, 7560, 0)
    SetChrPos(0xEF, -190, -250, 4550, 0)
    SetChrPos(0xF1, 1320, -250, 4470, 0)
    Jump("loc_4F00")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F00")
    SetChrPos(0xF1, 240, 250, 7560, 0)
    SetChrPos(0xEF, -190, -250, 4550, 0)
    SetChrPos(0xF0, 1320, -250, 4470, 0)

    label("loc_4F00")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #155
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F8")
    OP_A2(0x2C10)

    ChrTalk(    #156
        0x109,
        (
            "#1065F#6PBefore we go in here, Ries...there's something\x01",
            "I should warn you about.\x02\x03",

            "#1063FOnce we step through that door, there'll be no\x01",
            "going back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #157
        0x10F,
        "#1444F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x109,
        (
            "#1840F#6PYou're going to find out the truth about what\x01",
            "happened that day--all of it. And you won't like\x01",
            "it.\x02\x03",

            "Are you sure you're ready for what you're about\x01",
            "to find?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10F,
        "#1802F#11P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5204")

    label("loc_50F8")


    ChrTalk(    #160
        0x109,
        (
            "#1065F#6POnce we step through that door, there'll be no\x01",
            "going back.\x02\x03",

            "#1840FYou're going to find out the truth about what\x01",
            "happened that day--all of it. And you won't like\x01",
            "it.\x02\x03",

            "Are you sure you're ready for what you're about\x01",
            "to find?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #161
        0x10F,
        "#1802F#11P...\x02",
    )

    CloseMessageWindow()

    label("loc_5204")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E41")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Use Key\x01",      # 0
            "Don't\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_526B"),
        (SWITCH_DEFAULT, "loc_5E31"),
    )


    label("loc_526B")

    Sleep(300)

    ChrTalk(    #162
        0x10F,
        (
            "#1443F#11PI'm more than ready.\x02\x03",

            "#1445FAll these years, I've never quite been able to\x01",
            "accept what happened here.\x02\x03",

            "The life I thought I knew just suddenly came\x01",
            "to an end--with us all getting moved to other\x01",
            "places--and I still don't even know why...\x02\x03",

            "I even tried to come back here just before \x01",
            "beginning my training to become a squire,\x01",
            "but it had already been demolished.\x02\x03",

            "#1446FI've been ready for a long time. I want to\x01",
            "know the truth.\x02\x03",

            "#1806FAnd more than anything, I feel like knowing\x01",
            "will let me get closer to you and Rufina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x109,
        (
            "#1067F#6P...Okay.\x02\x03",

            "#1840FLet's head on in, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10F,
        "#1448F#11PRight.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xF)
    OP_73(0x0)
    Sleep(500)

    ChrTalk(    #165
        0x10F,
        "#1445F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5573")
    OP_A2(0x0)

    ChrTalk(    #166
        0x101,
        (
            "#1007F#6PU-Umm...\x02\x03",

            "#1025FShould the rest of us wait outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55D2")
    OP_A2(0x2)

    ChrTalk(    #167
        0x102,
        (
            "#1505F#6P...Kevin.\x02\x03",

            "#1502FShould the rest of us stay outside for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_55D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5675")

    ChrTalk(    #168
        0x104,
        (
            "#1545F#6PHmm... Kevin?\x02\x03",

            "#1540FI can't deny my overwhelming sense of curiosity,\x01",
            "but would it be best if the rest of us were to \x01",
            "wait outside?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5675")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D4")
    OP_A2(0x5)

    ChrTalk(    #169
        0x110,
        (
            "#267F#6PSay...\x02\x03",

            "...would it be best if the rest of us stayed\x01",
            "outside?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_56D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5731")
    OP_A2(0x1)

    ChrTalk(    #170
        0x107,
        (
            "#065F#6PU-Umm...\x02\x03",

            "#067FShould the rest of us wait outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5798")

    ChrTalk(    #171
        0x10E,
        (
            "#176F#6P...Kevin?\x02\x03",

            "#178FWould it best if the rest of us stayed outside\x01",
            "for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_580D")

    ChrTalk(    #172
        0x105,
        (
            "#1169F#6PUmm... Kevin...\x02\x03",

            "#1382FWould you prefer for the rest of us to wait \x01",
            "outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_580D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5867")

    ChrTalk(    #173
        0x103,
        (
            "#1526F#6PUmm...\x02\x03",

            "#1534FShould the rest of us wait outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58C9")

    ChrTalk(    #174
        0x106,
        (
            "#053F#6PHey, Kevin?\x02\x03",

            "#050FYou want the rest of us to wait outside\x01",
            "for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_58C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5926")
    OP_A2(0x4)

    ChrTalk(    #175
        0x10B,
        (
            "#215F#6PU-Umm...\x02\x03",

            "#212FShould the rest of us wait outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5983")
    OP_A2(0x3)

    ChrTalk(    #176
        0x10A,
        (
            "#813F#6PU-Umm...\x02\x03",

            "#810FShould the rest of us wait outside for this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5983")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E4")

    ChrTalk(    #177
        0x108,
        (
            "#074F#6PHmm...\x02\x03",

            "#070FDo you want the rest of us to wait outside for \x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_59E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A59")

    ChrTalk(    #178
        0x10C,
        (
            "#115F#6PIf I might ask...\x02\x03",

            "#110F...would you prefer for the rest of us to wait \x01",
            "outside for this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A59")


    def lambda_5A5F():
        OP_6D(-800, 250, 7000, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5A5F)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B18")

    ChrTalk(    #179
        0x109,
        (
            "#1075F#11PNo... Actually, I'd prefer if you came in with me.\x02\x03",

            "#1840FThis is relevant to you guys, too, in a sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B90")

    label("loc_5B18")


    ChrTalk(    #180
        0x109,
        (
            "#1075F#11PNo... Actually, I'd prefer if you came in with me.\x02\x03",

            "#1840FThis is relevant to you guys, too, in a sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B90")

    Sleep(300)
    Fade(500)
    OP_6D(0, 2500, 7460, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(0, 0)
    OP_6E(291, 0)
    SetChrPos(0x109, 40, -250, 5730, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C2C")
    SetChrPos(0xEF, 0, 250, 7770, 0)
    SetChrPos(0xF0, -570, -250, 4050, 0)
    SetChrPos(0xF1, 770, -250, 4000, 0)
    Jump("loc_5CB1")

    label("loc_5C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C70")
    SetChrPos(0xF0, 0, 250, 7770, 0)
    SetChrPos(0xEF, -570, -250, 4050, 0)
    SetChrPos(0xF1, 770, -250, 4000, 0)
    Jump("loc_5CB1")

    label("loc_5C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CB1")
    SetChrPos(0xF1, 0, 250, 7770, 0)
    SetChrPos(0xEF, -570, -250, 4050, 0)
    SetChrPos(0xF0, 770, -250, 4000, 0)

    label("loc_5CB1")

    OP_0D()
    OP_8C(0x109, 0, 400)

    def lambda_5CBF():
        OP_6D(0, 2250, 7460, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5CBF)

    def lambda_5CD7():
        OP_67(0, 3420, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_5CD7)

    def lambda_5CEF():
        OP_6B(2730, 6000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_5CEF)

    def lambda_5CFF():
        OP_6E(302, 6000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_5CFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D45")
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(200)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Jump("loc_5DBA")

    label("loc_5D45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D81")
    OP_43(0xF0, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Jump("loc_5DBA")

    label("loc_5D81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DBA")
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x12)

    label("loc_5DBA")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_22(0x178, 0x0, 0x64)
    OP_23(0x177)
    OP_B0(0x0, 0x8)
    OP_6F(0x0, 15)
    OP_70(0x0, 0x0)
    OP_23(0x177)
    OP_73(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    Call(0, 14)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7010   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E3E")

    label("loc_5E31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E3E")

    label("loc_5E3E")

    Jump("loc_5221")

    label("loc_5E41")

    EventEnd(0x0)
    Return()

    # Function_13_4DA5 end

    def Function_14_5E44(): pass

    label("Function_14_5E44")

    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E67")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E81")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5E81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E9B")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EB5")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ECF")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE9")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5EE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F03")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F1D")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F37")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F51")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F6B")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F85")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F9C")

    label("loc_5F85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9C")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F9C")

    Return()

    # Function_14_5E44 end

    def Function_15_5F9D(): pass

    label("Function_15_5F9D")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_5FB7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FB7)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_15_5F9D end

    def Function_16_5FDD(): pass

    label("Function_16_5FDD")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_5FF7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FF7)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_16_5FDD end

    def Function_17_601D(): pass

    label("Function_17_601D")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_6037():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6037)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_17_601D end

    def Function_18_605D(): pass

    label("Function_18_605D")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_6077():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6077)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_18_605D end

    def Function_19_609D(): pass

    label("Function_19_609D")

    EventBegin(0x1)
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 16777215, -1)

    def lambda_60BD():
        OP_90(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_60BD)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    NewScene("ED6_DT21/M4111   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_19_609D end

    SaveToFile()

Try(main)
