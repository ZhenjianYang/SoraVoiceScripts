from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4151   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4151.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Gilbert',                              # 9
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
        'ED6_DT07/CH02420 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02420P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_B6B",          # 03, 3
        "Function_4_BB2",          # 04, 4
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_EE")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_EE")

    Return()

    # Function_0_D2 end

    def Function_1_EF(): pass

    label("Function_1_EF")

    Return()

    # Function_1_EF end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 70000, 1720, 14920, 180)
    SetChrPos(0x10F, 70000, 1720, 14920, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 78160, 1250, 13000, 225)
    OP_6D(70110, 3350, 17060, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(390, 0)

    def lambda_18D():
        OP_6D(70110, 3350, 13660, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_18D)

    def lambda_1A5():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1A5)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(800)
    OP_43(0x10F, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    Sleep(3000)
    OP_44(0x10F, 0x2)
    Fade(1000)
    OP_6D(70700, 250, 5590, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(44000, 0)
    OP_6E(344, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1068F#6PI thought you were joking when you said you\x01",
            "were going to buy everything they had left...\x02\x03",

            "The girl behind the counter looked like she\x01",
            "thought you were a freak of nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1442F#2PThis is just another example of Aidios' divine\x01",
            "providence.\x02\x03",

            "It's better that they're bought by someone who\x01",
            "intends to consume them than to have the poor\x01",
            "things be thrown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1840F#6PYeah, yeah. You're a real bleeding heart.\x01",
            "But THAT much?\x02\x03",

            "I hope you're not spending your entire salary\x01",
            "on food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1447F#2PI'll have you know that you have nothing to\x01",
            "worry about.\x02\x03",

            "There are few people in this world who know\x01",
            "how to make better use of sales and special\x01",
            "offers than I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1840F#6P*sigh* Well, whatever makes you happy. It's not\x01",
            "my business how you blow your mira at the end\x01",
            "of the day.\x02\x03",

            "#1068FStill, while I'll give you that my getup is right up\x01",
            "the top of the 'suspicious' charts...\x02\x03",

            "...I'm pretty sure anyone would be confused if\x01",
            "a woman in a sister's habit came wandering into\x01",
            "their shop after dark to buy out the leftovers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1801F#2POh, stop your grumbling.\x02\x03",

            "#1447F...And it's almost time for us to leave. We should\x01",
            "make our way over to the landing port.\x02\x03",

            "I'm not sure how much longer my stomach can\x01",
            "wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1840F#6PYes, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x109,
        "#1063F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1444F#2PIs someth...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(79250, 1250, 14670, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)

    def lambda_7F1():
        OP_8F(0xFE, 0x13150, 0x4E2, 0x3B74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F1)
    OP_0D()
    Sleep(1500)

    def lambda_812():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_812)
    OP_6D(70700, 250, 5590, 3000)
    Sleep(300)

    ChrTalk(    #9
        0x10F,
        "#1801F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1840F#6P(Sorry. That stomach of yours is gonna\x01",
            "have to wait a little longer.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#2P(Unforgivable...)\x02\x03",

            "#1801F(I don't know who this fiend is, but as long\x01",
            "as I don't kill them, I can go as far as I like,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x109,
        (
            "#1068F#6P(I sympathize, but you...uh...might wanna\x01",
            "calm down a little.)\x02\x03",

            "#1060F(Still, whoever they are, they're not very good\x01",
            "at tailing people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1443F#2P(Quite. I doubt they have much experience.)\x02\x03",

            "(They do seem to have undergone some degree\x01",
            "of training, however.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P(Yeah...)\x02\x03",

            "#1063F(Oh, well. Sad to say, but we're going to have\x01",
            "to skip today's last airship out of here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1443F#2P(Do you know of a good place to strike?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1075F#6P(Oh, I do.)\x02\x03",

            "#1060F(I know the perfect place.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4404   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_F0 end

    def Function_3_B6B(): pass

    label("Function_3_B6B")


    def lambda_B71():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B71)
    OP_8E(0xFE, 0x11260, 0x4E2, 0x3156, 0x7D0, 0x0)
    OP_8E(0xFE, 0x113FA, 0xFA, 0x1202, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_B6B end

    def Function_4_BB2(): pass

    label("Function_4_BB2")


    def lambda_BB8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB8)
    OP_8E(0xFE, 0x110A8, 0x4E2, 0x3156, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x1194, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_BB2 end

    SaveToFile()

Try(main)
