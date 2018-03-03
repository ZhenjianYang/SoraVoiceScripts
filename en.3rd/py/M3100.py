from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3100   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        TriggerX            = 3630,
        TriggerZ            = -20,
        TriggerY            = -49100,
        TriggerRange        = 1000,
        ActorX              = 3630,
        ActorZ              = 2000,
        ActorY              = -49100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_151",          # 02, 2
        "Function_3_FC5",          # 03, 3
        "Function_4_1247",         # 04, 4
        "Function_5_13DE",         # 05, 5
        "Function_6_1539",         # 06, 6
        "Function_7_164F",         # 07, 7
        "Function_8_169D",         # 08, 8
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_107")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_11F"),
        (SWITCH_DEFAULT, "loc_126"),
    )


    label("loc_11F")

    Event(0, 4)
    Jump("loc_126")

    label("loc_126")

    Return()

    # Function_0_F2 end

    def Function_1_127(): pass

    label("Function_1_127")

    OP_22(0x1CC, 0x0, 0x64)
    OP_1B(0x3, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_END)), "loc_150")
    OP_6F(0x0, 450)

    label("loc_150")

    Return()

    # Function_1_127 end

    def Function_2_151(): pass

    label("Function_2_151")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 880, 0, -54890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6")
    SetChrPos(0xEF, 100, -110, -53600, 0)
    SetChrPos(0xF0, -1120, -40, -54830, 0)
    SetChrPos(0xF1, -140, 0, -55760, 0)
    Jump("loc_23B")

    label("loc_1B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    SetChrPos(0xF0, 100, -110, -53600, 0)
    SetChrPos(0xEF, -1120, -40, -54830, 0)
    SetChrPos(0xF1, -140, 0, -55760, 0)
    Jump("loc_23B")

    label("loc_1FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    SetChrPos(0xF1, 100, -110, -53600, 0)
    SetChrPos(0xEF, -1120, -40, -54830, 0)
    SetChrPos(0xF0, -140, 0, -55760, 0)

    label("loc_23B")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(500, -70, -54070, 0)
    OP_67(0, 8480, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AA)

    def lambda_3BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BC)

    def lambda_3CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3CE)

    def lambda_3E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3E0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_45D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_485")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49C")

    label("loc_485")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_49C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_519")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_530")

    label("loc_519")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_530")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C4")

    label("loc_5AD")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5C4")

    Sleep(1500)

    ChrTalk(    #0
        0x10C,
        (
            "#119F#6PNow that riddle makes sense...\x02\x03",

            "#118FWhat better place to describe as an impregnable\x01",
            "fortress than this?\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xE8)
    Sleep(300)
    Fade(1000)
    OP_6D(1360, -100, -50470, 0)
    OP_67(0, 10030, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(45000, 0)
    OP_6E(378, 0)

    def lambda_68E():
        OP_6D(0, 3000, -1700, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_68E)

    def lambda_6A6():
        OP_67(0, 8200, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6A6)

    def lambda_6BE():
        OP_6B(3390, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6BE)

    def lambda_6CE():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6CE)

    def lambda_6DE():
        OP_6E(387, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_6DE)
    OP_C8(0x200, 0x46, "C_PLAC35._CH", 0x1, 0xBB8)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E")

    def lambda_716():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_716)
    Sleep(50)

    def lambda_736():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_736)
    Sleep(150)

    def lambda_756():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_756)
    Sleep(50)

    def lambda_776():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_776)
    Jump("loc_8A3")

    label("loc_78E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")

    def lambda_7A2():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7A2)
    Sleep(50)

    def lambda_7C2():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C2)
    Sleep(150)

    def lambda_7E2():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7E2)
    Sleep(50)

    def lambda_802():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_802)
    Jump("loc_8A3")

    label("loc_81A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A3")

    def lambda_82E():
        OP_8F(0xFE, 0xFFFFFD8A, 0xFFFFFF7E, 0xFFFF5150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_82E)
    Sleep(50)

    def lambda_84E():
        OP_8F(0xFE, 0x276, 0xFFFFFF56, 0xFFFF50A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_84E)
    Sleep(150)

    def lambda_86E():
        OP_8F(0xFE, 0x2A8, 0xFFFFFF06, 0xFFFF4B92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_86E)
    Sleep(50)

    def lambda_88E():
        OP_8F(0xFE, 0xFFFFFCEA, 0xFFFFFF6A, 0xFFFF4B2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_88E)

    label("loc_8A3")

    WaitChrThread(0xEF, 0x1)

    def lambda_8AE():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8AE)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    WaitChrThread(0xEE, 0x1)

    def lambda_8D6():
        OP_6D(0, 3300, -500, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8D6)

    def lambda_8EE():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_8EE)

    def lambda_906():
        OP_6B(3900, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_906)

    def lambda_916():
        OP_6E(410, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_916)
    Sleep(1000)
    OP_22(0x6C, 0x0, 0x64)
    WaitChrThread(0xEE, 0x1)
    OP_73(0x0)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    Sleep(300)
    Fade(1000)
    OP_6D(1110, -150, -44470, 0)
    OP_67(0, 7470, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(266, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A76")

    ChrTalk(    #1
        0x10F,
        "#1802F#12PWhere are we, Kevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1065F#5PThis is Leiston Fortress, the biggest Royal Army\x01",
            "stronghold in the country.\x02\x03",

            "#1063FAnd I can already tell we're gonna get a real fun\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1443F#4P...That we are.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE2")

    label("loc_A76")


    ChrTalk(    #4
        0x109,
        (
            "#1065F#5PGood ol' Leiston Fortress, huh?\x02\x03",

            "#1063FI can already tell we're gonna get a real fun\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE2")


    ChrTalk(    #5
        0x10C,
        (
            "#119F#5PHaha. Well, aren't we in for a treat?\x02\x03",

            "I think it's safe to say that whoever is waiting\x01",
            "for us--and I can think of a few who may be--\x01",
            "we're going to need to give the battles our all.\x02\x03",

            "#110FThis isn't an area we can conquer with anything\x01",
            "less than top form.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C21")

    ChrTalk(    #6
        0x101,
        "#1020F#12PTell me about it...\x02",
    )

    CloseMessageWindow()

    label("loc_C21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")

    ChrTalk(    #7
        0x105,
        "#1162F#12PAgreed.\x02",
    )

    CloseMessageWindow()

    label("loc_C46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6B")

    ChrTalk(    #8
        0x103,
        "#1525F#12PAgreed.\x02",
    )

    CloseMessageWindow()

    label("loc_C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8F")

    ChrTalk(    #9
        0x108,
        "#074F#12PAgreed.\x02",
    )

    CloseMessageWindow()

    label("loc_C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC8")

    ChrTalk(    #10
        0x10A,
        "#1317F#12PTh-This is just cheating...\x02",
    )

    CloseMessageWindow()

    label("loc_CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0E")

    ChrTalk(    #11
        0x102,
        "#1502F#12PThis is going to be quite a challenge...\x02",
    )

    CloseMessageWindow()

    label("loc_D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D61")

    ChrTalk(    #12
        0x10E,
        (
            "#178F#12PI've been here many a time, but never\x01",
            "as an aggressor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9F")

    ChrTalk(    #13
        0x104,
        "#1545F#12PWhat an interesting development.\x02",
    )

    CloseMessageWindow()

    label("loc_D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(    #14
        0x10D,
        (
            "#278F#12PThis fortress has an intimidating reputation...\x02\x03",

            "#277F...and I, for one, look forward to seeing how\x01",
            "much its defenses live up to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA7")

    ChrTalk(    #15
        0x10B,
        (
            "#413F#12POh, fun... I can't say I've got anything but bad\x01",
            "memories of this place...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F12")

    ChrTalk(    #16
        0x106,
        (
            "#051F#12PHeh. How often do you get to say you bashed\x01",
            "your way into this fortress twice?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F64")

    ChrTalk(    #17
        0x107,
        (
            "#065F#12PAre we going to have to fight lots of soldiers\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAB")

    ChrTalk(    #18
        0x110,
        "#1306F#12PHeehee. I can hardly wait to get started.\x02",
    )

    CloseMessageWindow()

    label("loc_FAB")

    OP_A2(0x2B18)
    OP_28(0x39, 0x1, 0x8)
    Sleep(300)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_2_151 end

    def Function_3_FC5(): pass

    label("Function_3_FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1094")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6400)
    Sleep(500)
    Jump("loc_1097")

    label("loc_1094")

    TalkBegin(0xFF)

    label("loc_1097")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1216")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_112F"),
        (1, "loc_11AA"),
        (2, "loc_11D8"),
        (SWITCH_DEFAULT, "loc_1206"),
    )


    label("loc_112F")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1213")

    label("loc_11AA")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #20
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1213")

    label("loc_11D8")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1213")

    label("loc_1206")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1213")

    label("loc_1213")

    Jump("loc_10D3")

    label("loc_1216")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1243")
    OP_A2(0x259C)
    EventEnd(0x1)
    Jump("loc_1246")

    label("loc_1243")

    TalkEnd(0xFF)

    label("loc_1246")

    Return()

    # Function_3_FC5 end

    def Function_4_1247(): pass

    label("Function_4_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1258")
    Call(0, 2)
    Return()

    label("loc_1258")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 100, -110, -53600, 0)
    SetChrPos(0x1, 880, 0, -54890, 0)
    SetChrPos(0x2, -1120, -40, -54830, 0)
    SetChrPos(0x3, -140, 0, -55760, 0)
    OP_69(0x0, 0x0)
    OP_6C(45000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_4_1247 end

    def Function_5_13DE(): pass

    label("Function_5_13DE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 100, -110, -53600, 180)
    SetChrPos(0x2, 880, 0, -54890, 180)
    SetChrPos(0x1, -1120, -40, -54830, 180)
    SetChrPos(0x0, -140, 0, -55760, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    NewScene("ED6_DT21/M4112   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_13DE end

    def Function_6_1539(): pass

    label("Function_6_1539")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1562")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1556():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1556)

    label("loc_1562")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158B")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_157F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_157F)

    label("loc_158B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_15A8)

    label("loc_15B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DD")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_15D1)

    label("loc_15DD")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1609")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1609")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1620")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1620")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1637")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1637")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_164E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_164E")

    Return()

    # Function_6_1539 end

    def Function_7_164F(): pass

    label("Function_7_164F")


    def lambda_1655():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1655)

    def lambda_1667():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1667)

    def lambda_1679():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1679)

    def lambda_168B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_168B)
    Sleep(1000)
    Return()

    # Function_7_164F end

    def Function_8_169D(): pass

    label("Function_8_169D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x05                Warning! \x01",
            "Restricted Area -- Photography Prohibited\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_169D end

    SaveToFile()

Try(main)
