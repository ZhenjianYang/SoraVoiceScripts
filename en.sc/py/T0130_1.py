from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0130_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_B34",          # 01, 1
        "Function_2_CD7",          # 02, 2
        "Function_3_1EB3",         # 03, 3
        "Function_4_26E4",         # 04, 4
        "Function_5_27DC",         # 05, 5
        "Function_6_28A8",         # 06, 6
        "Function_7_303A",         # 07, 7
        "Function_8_3F9B",         # 08, 8
        "Function_9_3FEA",         # 09, 9
        "Function_10_4032",        # 0A, 10
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1AE")

    ChrTalk(    #0
        0xFE,
        (
            "#6PHmmm... The grand cathedral's hard\x01",
            "to toss aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "#6PBut I guess I really would rather we\x01",
            "have our wedding here in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "#6PTo swear our love at the place we met\x01",
            "may sound kinda cliche, but there's a\x01",
            "holy sense to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B7")

    label("loc_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_21E")

    ChrTalk(    #3
        0xFE,
        "#6PAh, my adorable Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "#6PJust as the fog engulfs the city,\x01",
            "I am wrapped in your love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B7")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_272")

    ChrTalk(    #5
        0xFE,
        "#6PCome closer, Ellie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#6PI want to see nothing but your smile.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B7")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3B7")

    ChrTalk(    #7
        0xFE,
        (
            "#6PAhh, that wonderful evening during\x01",
            "the Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "#6PEllie... Every time I see your face,\x01",
            "the emotions from that night come\x01",
            "flooding back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "#6PWe gazed at each other underneath the\x01",
            "lights of the stars and the fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "#6PI put my dedication into words,\x01",
            "and conveyed them to you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7")


    ChrTalk(    #11
        0x101,
        (
            "#1007F#6PAhem!\x02\x03",

            "Ummm, may I have a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #12
        0xF,
        "#6PHmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_414():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_414)
    Sleep(250)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #13
        0x10,
        "#2POh? Who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1000F#6PI'm with the Bracer Guild.\x02\x03",

            "You're Armand, right? I saw your\x01",
            "request on the bulletin board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        "Ah, you really came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        "Thank you! I've been waiting so long!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #17
        0x10,
        (
            "#2PThis is wonderful, Armand!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #18
        0xF,
        "#6PAhh, Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        "#6PWhy is your heart so beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "#6PEven though I am the cause of\x01",
            "your suffering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#2PDon't say that, Armand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#2PI know best just how hard this\x01",
            "is on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#2PWe promised on that night, didn't we?\x01",
            "That you and I, no matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "#6PWe would hold hands and live out\x01",
            "our days together, good and bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xF,
        "#6POh, I love you, Ellie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#2PAnd I you, Armand!\x02",
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_784")

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_784")

    label("loc_76D")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AB")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_7E9")

    label("loc_7AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D2")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_7E9")

    label("loc_7D2")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_7E9")

    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1016F#6PUmmmm...\x02\x03",

            "Didn't you have some kind of request?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #28
        0xF,
        "#6PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#2PThat's right, the request!\x02",
    )

    CloseMessageWindow()

    def lambda_87B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_87B)
    Sleep(150)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #30
        0xF,
        (
            "W-Well, to make it short, this request\x01",
            "is so important that it directly affects\x01",
            "our future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xF,
        (
            "In fact, I'd like you to start investigating\x01",
            "immediately if you can. Can you?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    Call(1, 2)
    Jump("loc_B1B")

    label("loc_994")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#6PAh, er, sorry.\x02\x03",

            "I'm afraid we can't start right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        "N-Nooo... Don't abandon us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "#2PPlease... This is very important!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x103,
        (
            "#020FIt's okay. We'll be back soon,\x01",
            "so please relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1000F#6PYeah, we'll be back the second\x01",
            "we have time to hear what you\x01",
            "have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xF,
        "R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        "A-All right... I believe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#2PCome back soon, please.\x01",
            "For our love!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x8000)

    label("loc_B1B")

    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_B34(): pass

    label("Function_1_B34")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_8C(0xF, 270, 0)
    OP_8C(0x10, 270, 0)
    OP_0D()

    ChrTalk(    #40
        0xF,
        "Oh, hello again, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "Are you ready to hear our\x01",
            "request?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    Call(1, 2)
    Jump("loc_CBE")

    label("loc_BE6")


    ChrTalk(    #42
        0x101,
        "#1007F#6PTo be honest, we're still a bit busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        "N-Nooooooooooo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1016F#6PSorry, sorry! I know it's important.\x01",
            "We'll be back to hear you out soon,\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "Come back soon, please.\x01",
            "For our love!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBE")

    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_1_B34 end

    def Function_2_CD7(): pass

    label("Function_2_CD7")


    ChrTalk(    #46
        0x101,
        "#1006F#6PYep! We're all squared away.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE1")

    ChrTalk(    #47
        0xF,
        "R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020FWe're in a hurry, though,\x01",
            "so make it quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xF,
        "Of course, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "Bless you, bracers! Bless your\x01",
            "loving hearts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "You have NO idea how much\x01",
            "I appreciate you doing this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E24")

    label("loc_DE1")


    ChrTalk(    #52
        0xF,
        "R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "Bless you, bracers! Bless your\x01",
            "loving hearts!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E24")

    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #54
        0x10,
        (
            "#2PHow wonderful, Armand!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #55
        0xF,
        "#6PAhh, Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xF,
        "#6PWhy is your heart so beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#2POooh, Armand...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        (
            "#6P#1019F#4SSo...#2S\x02\x03",

            "...about that request.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EF2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_EF2)
    Sleep(150)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #59
        0xF,
        "...Pardon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        "Ahem! Yes. Let me explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#020FYes, please do.\x01",
            "As simply and swiftly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        (
            "What I'd like to ask of you all\x01",
            "is nothing less than finding our\x01",
            "engagement ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xF,
        (
            "I scraped and saved up all the\x01",
            "mira I could to get a really nice\x01",
            "ring, but then...then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xF,
        (
            "Th-That cursed crow snatched\x01",
            "it from me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x101,
        "#6P#1004FC-Crow?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BB")

    ChrTalk(    #66
        0x107,
        "#064FCrow? Like a bird?\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_10BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F5")

    ChrTalk(    #67
        0x105,
        "#044FYou mean like the bird, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_10F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1126")

    ChrTalk(    #68
        0x104,
        "#033FCrow? As in the bird?\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_1126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115D")

    ChrTalk(    #69
        0x106,
        "#052FYou mean like the bird, right?\x02",
    )

    CloseMessageWindow()

    label("loc_115D")


    ChrTalk(    #70
        0xF,
        (
            "Yes! The ones that go, 'caw!'\x01",
            "and bring suffering to those\x01",
            "in love!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xF,
        (
            "One of those dastardly things\x01",
            "flew off with our ring in his mouth!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1657")

    ChrTalk(    #72
        0x103,
        (
            "#026FHa. Well, crows are known to\x01",
            "have an eye for anything shiny.\x02\x03",

            "#027FStill... A ring and a crow... Hmm...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #73
        0x101,
        (
            "#7P#1011FHmm?\x02\x03",

            "Schera, are you thinking what\x01",
            "I'm thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020FI believe I am. We should have\x01",
            "them take a look just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xF,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xF,
        "Did you think of something?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #77
        0x101,
        (
            "#6P#1002FArmand, would you take\x01",
            "a look at this ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78 op#A
        0xF,
        (
            "#22ASure, I don't mi...\x01",
            "WHOA! THIS IS IT!\x02",
        )
    )
    Sleep(2300)

    Call(1, 5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x101,
        "#6P#1004FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1404")

    ChrTalk(    #80
        0x107,
        "#064FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_1404")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142F")

    ChrTalk(    #81
        0x105,
        "#044FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_142F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1458")

    ChrTalk(    #82
        0x104,
        "#033FAre you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_1458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147D")

    ChrTalk(    #83
        0x106,
        "#055FYou sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_147D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(    #84
        0x108,
        "#073FYou sure?\x02",
    )

    CloseMessageWindow()

    label("loc_149F")


    ChrTalk(    #85
        0xF,
        "Yes, I'm ABSOLUTELY sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xF,
        "This is our ring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        (
            "#2PI cannot thank you enough for\x01",
            "your kindness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        (
            "#021FLooks like my hunch was right\x01",
            "on the mira.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157A")

    ChrTalk(    #89
        0x108,
        "#073FTalk about a crazy coincidence.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1624")

    label("loc_157A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B5")

    ChrTalk(    #90
        0x106,
        "#052FTalk about a crazy coincidence.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1624")

    label("loc_15B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #91
        0x104,
        "#031FHahaha. My, how serendipitous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1624")

    label("loc_15EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1624")

    ChrTalk(    #92
        0x105,
        "#044FWhat an amazing coincidence!\x02",
    )

    CloseMessageWindow()

    label("loc_1624")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x8)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_63(0x29)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_1EB2")

    label("loc_1657")


    ChrTalk(    #93
        0x103,
        (
            "#027FHa. Well, crows are known to\x01",
            "have an eye for anything shiny.\x02\x03",

            "A sparkling ring sounds just like\x01",
            "their idea of a new toy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#6P#1015FThat ring's probably in some\x01",
            "bird's nest by now, huh?\x02\x03",

            "#1002FAnd you want us to find it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xF,
        "Please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "I'm well aware of how much of \x01",
            "a challenge this is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xF,
        (
            "Even so, I dearly hope you'll find it.\x01",
            "Somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1007F#6PI mean, I want to find it, too, but...\x02\x03",

            "We don't have a whole lot of info\x01",
            "to work with here. Just knowing a\x01",
            "crow took it isn't all that much.\x02\x03",

            "#1002FDo you have any more clues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xF,
        (
            "Well, I have some idea of where\x01",
            "its nest is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        "I'm pretty sure it's north of Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xF,
        (
            "The crow flew off towards the\x01",
            "Malga Trail after it was done\x01",
            "plundering our hopes and dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "I would have given chase, but with\x01",
            "the fog and all...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ACF")

    ChrTalk(    #103
        0x101,
        (
            "#1015F#6PHa, no worries. I understand.\x02\x03",

            "So the nest's probably to the north...\x02\x03",

            "...Wait? To the north?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #104
        0x101,
        (
            "#1019F#6P(N-No way!)\x02\x03",

            "(What if it's that ring we found\x01",
            "at the top of the tower?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xF,
        "Mm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1016F#6PN-No, it's nothing.\x01",
            "(Eh, I'm sure it's just a coincidence.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1ACF")


    ChrTalk(    #107
        0x101,
        (
            "#1015F#6PI see.\x02\x03",

            "So the nest's probably to the north...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0C")


    ChrTalk(    #108
        0x103,
        (
            "#026FWe'll take that under advisement.\x02\x03",

            "Anyway, seems we have no choice\x01",
            "but to investigate places where the\x01",
            "nest is likely to be.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C00")

    ChrTalk(    #109
        0x108,
        (
            "#075FYeah, no other leads, really.\x02\x03",

            "This request is going to be\x01",
            "a real pain, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D31")

    label("loc_1C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(    #110
        0x106,
        (
            "#551FYeah, got no other choice.\x02\x03",

            "This is gonna be a pain in the\x01",
            "ass...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D31")

    label("loc_1C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF1")

    ChrTalk(    #111
        0x104,
        (
            "#034FNot much else we can do, really.\x02\x03",

            "*sigh* This looks like a job that's\x01",
            "going to require a lot of finesse...\x01",
            "and patience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D31")

    label("loc_1CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D31")

    ChrTalk(    #112
        0x105,
        (
            "#047FAfraid there isn't much else we\x01",
            "CAN do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D31")


    ChrTalk(    #113
        0xF,
        (
            "We have no choice but to rely\x01",
            "on the guild at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xF,
        (
            "Please, PLEASE do everything\x01",
            "you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#2PYou bracers are our only hope.\x01",
            "Please, you must find it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1006F#6PWe'll do whatever we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#020FWe'll come back and report\x01",
            "once we know more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        (
            "We'll be right here! Our hope\x01",
            "--and our future--rests with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "#2PGood luck!\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x4, 0x4)
    OP_28(0x72, 0x4, 0x8)
    OP_28(0x72, 0x1, 0x1)
    OP_28(0x72, 0x1, 0x2)
    OP_A2(0xB)
    ClearChrFlags(0xF, 0x10)

    label("loc_1EB2")

    Return()

    # Function_2_CD7 end

    def Function_3_1EB3(): pass

    label("Function_3_1EB3")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1FB7")

    ChrTalk(    #120
        0xFE,
        (
            "#6PHmmm... The grand cathedral's hard\x01",
            "to toss aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "#6PBut I guess I really would rather we\x01",
            "have our wedding here in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "#6PTo swear our love at the place we met\x01",
            "may sound kinda cliche, but there's a\x01",
            "holy sense to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C0")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2027")

    ChrTalk(    #123
        0xFE,
        "#6PAh, my adorable Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "#6PJust as the fog engulfs the city,\x01",
            "I am wrapped in your love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C0")

    label("loc_2027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_207B")

    ChrTalk(    #125
        0xFE,
        "#6PCome closer, Ellie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#6PI want to see nothing but your smile.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C0")

    label("loc_207B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_21C0")

    ChrTalk(    #127
        0xFE,
        (
            "#6PAhh, that wonderful evening during\x01",
            "the Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "#6PEllie... Every time I see your face,\x01",
            "the emotions from that night come\x01",
            "flooding back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "#6PWe gazed at each other underneath the\x01",
            "lights of the stars and the fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "#6PI put my dedication into words,\x01",
            "and conveyed them to you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C0")


    ChrTalk(    #131
        0x101,
        "#6P#1007F(They're still at it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xF,
        "#6PHmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_21FD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21FD)
    Sleep(250)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #133
        0x10,
        "#2PYou're back!\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xF)

    ChrTalk(    #134
        0xF,
        "D-Did you find our ring?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        (
            "#020FWe've found a ring that matches\x01",
            "your description, at least.\x02\x03",

            "We'll need to have you identify it\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#6P#1000FYep. We just need you to confirm\x01",
            "if it's yours or not.\x02\x03",

            "Armand, could you take a look at\x01",
            "this ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137 op#A
        0xF,
        "#22ASure, I don't mi...\x02",
    )
    Sleep(2000)

    Call(1, 5)

    ChrTalk(    #138
        0x101,
        "#6P#1004FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A3")

    ChrTalk(    #139
        0x107,
        "#064FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2444")

    label("loc_23A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CE")

    ChrTalk(    #140
        0x105,
        "#044FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2444")

    label("loc_23CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F9")

    ChrTalk(    #141
        0x104,
        "#033FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2444")

    label("loc_23F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2422")

    ChrTalk(    #142
        0x106,
        "#055FAre you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2444")

    label("loc_2422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2444")

    ChrTalk(    #143
        0x108,
        "#073FYou sure?\x02",
    )

    CloseMessageWindow()

    label("loc_2444")


    ChrTalk(    #144
        0xF,
        "You sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xF,
        "Yes, I'm ABSOLUTELY sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10,
        (
            "#2PI cannot thank you enough for\x01",
            "your kindness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x103,
        (
            "#021FGood to hear! Makes this all\x01",
            "worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253B")

    ChrTalk(    #148
        0x108,
        (
            "#070FMission complete!\x02\x03",

            "Didn't expect we'd find it in\x01",
            "such a bizarre spot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B9")

    label("loc_253B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B9")

    ChrTalk(    #149
        0x105,
        (
            "#040FGood... That settles things, then.\x02\x03",

            "I never dreamed we would find it\x01",
            "in a place like that, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B9")

    label("loc_25B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2640")

    ChrTalk(    #150
        0x106,
        (
            "#051FGood to hear. Nice to finally\x01",
            "wrap this thing up.\x02\x03",

            "Never thought we'd find it in\x01",
            "such a weird spot, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B9")

    label("loc_2640")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B9")

    ChrTalk(    #151
        0x104,
        (
            "#030FA job well done!\x02\x03",

            "I certainly never dreamed the\x01",
            "request would take us where\x01",
            "we ended up, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B9")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_63(0x29)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_3_1EB3 end

    def Function_4_26E4(): pass

    label("Function_4_26E4")

    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    SetChrPos(0x101, 62800, 0, 47270, 90)
    SetChrPos(0x103, 61790, 0, 46800, 90)
    SetChrPos(0xF8, 61270, 0, 47980, 90)
    SetChrPos(0xF9, 60320, 0, 47290, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275F")
    SetChrPos(0xF9, 61270, 0, 47980, 90)
    SetChrPos(0xF8, 60320, 0, 47290, 90)

    label("loc_275F")

    OP_6D(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_51(0x29, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_26E4 end

    def Function_5_27DC(): pass

    label("Function_5_27DC")

    OP_94(0x1, 0xF, 0x0, 0xC8, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_2810():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2810)
    Sleep(900)
    OP_63(0xF)
    WaitChrThread(0xF, 0x1)

    ChrTalk(    #152
        0xF,
        "#3SAaaaaaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xF,
        "Th-Th-That's the ring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xF,
        "#3SThat's it! That's our engagement ring!!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_5_27DC end

    def Function_6_28A8(): pass

    label("Function_6_28A8")


    ChrTalk(    #155
        0x101,
        (
            "#6P#1015FPhew! Man...\x02\x03",

            "Yeah, never thought we'd find\x01",
            "your ring on the roof of the tower.\x02\x03",

            "#1000FHere, let me give it back to you\x01",
            "before it ends up lost again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #156
        "\x07\x00Handed over #564i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x234, 1)
    OP_94(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #157
        0xF,
        "Th-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xF,
        (
            "I... I don't even know how to express\x01",
            "how I feel right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10,
        (
            "#2PTeehee! We never lost our faith\x01",
            "in you. Thank you so, so much. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#6P#1017FNot at all. I'm glad we could help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x103,
        (
            "#020FYour wedding isn't too far off\x01",
            "from now, is it?\x02\x03",

            "#525FBest wishes! ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #162
        0x10,
        "#2PTh-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        (
            "#2PGoodness, it's a little embarrassing\x01",
            "to hear it said out loud...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #164
        0xF,
        "#6PDon't be embarrassed, my love.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xF,
        (
            "#6PFor no other love has received a\x01",
            "stronger blessing. We still have\x01",
            "a lifetime of well wishes ahead of us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #166
        0x10,
        "#2PArmand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xF,
        "#6PEllie...\x02",
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 1800, 0xA, 0xB, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7A")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2CB8")

    label("loc_2C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA1")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2CB8")

    label("loc_2CA1")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDF")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2D1D")

    label("loc_2CDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D06")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2D1D")

    label("loc_2D06")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2D1D")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D6E")

    ChrTalk(    #168
        0x107,
        (
            "#067F(Awww...\x01",
            "They're off in their own little world.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3A")

    label("loc_2D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB3")

    ChrTalk(    #169
        0x105,
        "#540F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E3A")

    label("loc_2DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DF8")

    ChrTalk(    #170
        0x104,
        "#030F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E3A")

    label("loc_2DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E3A")

    ChrTalk(    #171
        0x108,
        "#070F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()

    label("loc_2E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E79")

    ChrTalk(    #172
        0x106,
        "#552F(Watching this makes my head hurt.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F24")

    label("loc_2E79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EAC")

    ChrTalk(    #173
        0x108,
        "#071F(Truly, love is blind.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F24")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF0")

    ChrTalk(    #174
        0x104,
        "#031F(You know what they say: Love is blind.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F24")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F24")

    ChrTalk(    #175
        0x105,
        "#048F(Haha, I think it's sweet.)\x02",
    )

    CloseMessageWindow()

    label("loc_2F24")


    ChrTalk(    #176
        0x103,
        (
            "#020F(Anyway, it'd be rude to interrupt them,\x01",
            "so...let's excuse ourselves.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#6P#1013F(Yes! Good idea! Let's go, go, go!)\x02\x03",

            "#1016FWell, pardon us, lovebirds.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #178
        "Quest #2C[The Ring That Flew Away] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    OP_A2(0xC)
    Return()

    # Function_6_28A8 end

    def Function_7_303A(): pass

    label("Function_7_303A")

    EventBegin(0x0)
    OP_EA(0x1, 0x3, 0x0, 0x0)
    OP_D2(0x700A8, 0x700AC, 0x8)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, -17310, 0, 42890, 270)
    SetChrPos(0x11, -15330, 0, 42890, 270)
    SetChrPos(0x101, -16070, 0, 44880, 180)
    SetChrPos(0x103, -15100, 0, 45270, 180)
    SetChrPos(0xF8, -16480, 0, 46150, 180)
    SetChrPos(0xF9, -15220, 0, 46480, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E5")
    SetChrPos(0xF9, -16480, 0, 46150, 180)
    SetChrPos(0xF8, -15220, 0, 46480, 180)

    label("loc_30E5")

    OP_6D(-17110, 0, 44470, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 255)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_8F(0x8, 0xFFFFBE42, 0x0, 0xA78A, 0x3E8, 0x0)

    ChrTalk(    #179
        0x8,
        "#6P...Hmm.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11, 400)

    ChrTalk(    #180
        0x8,
        "Thank you for waiting. The medicine is done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        "Here, take it. This is Diaset's Secret.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0xFFFFC2A2, 0x0, 0xA78A, 0x3E8, 0x0)

    ChrTalk(    #182
        0x11,
        (
            "*g-gulp* This is the medicine\x01",
            "I've been looking for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "This is it! A medicine to keep you from\x01",
            "getting drunk, no matter how much you\x01",
            "drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        "That is true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "However, that effect is only applicable\x01",
            "if you follow all directions and use the\x01",
            "correct dosa--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186 op#A
        0x11,
        (
            "#38A#3SYAHOOO!!#2000W #20W\x01",
            "I've finally got it!\x02",
        )
    )
    Sleep(2300)

    SetChrFlags(0x11, 0x20)

    def lambda_331C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_331C)
    OP_8C(0x11, 0, 1600)
    OP_8C(0x11, 90, 1600)
    OP_8C(0x11, 180, 1600)
    OP_8C(0x11, 270, 1600)
    OP_8C(0x11, 0, 1600)
    OP_8C(0x11, 90, 1600)
    OP_8C(0x11, 180, 1600)
    OP_8C(0x11, 270, 1600)
    WaitChrThread(0x11, 0x0)
    ClearChrFlags(0x11, 0x20)
    Sleep(500)

    ChrTalk(    #187
        0x11,
        (
            "#3SNow I can confess my feelings to\x01",
            "Aina with my head held high!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E8")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3426")

    label("loc_33E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340F")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3426")

    label("loc_340F")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344D")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_348B")

    label("loc_344D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3474")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_348B")

    label("loc_3474")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_348B")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B7")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_34F5")

    label("loc_34B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34DE")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_34F5")

    label("loc_34DE")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_34F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_355A")

    label("loc_351C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3543")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_355A")

    label("loc_3543")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_355A")

    Sleep(800)

    ChrTalk(    #188
        0x101,
        "#1004F#4P#3SWhaaaaaaaaaaat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A6")

    ChrTalk(    #189
        0x107,
        "#064FWh-Wh-What?!\x02",
    )

    CloseMessageWindow()

    label("loc_35A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C9")

    ChrTalk(    #190
        0x105,
        "#044FOh, my...!\x02",
    )

    CloseMessageWindow()

    label("loc_35C9")


    ChrTalk(    #191
        0x103,
        "#023FD-Did he just say Aina?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3623")

    ChrTalk(    #192
        0x106,
        "#052F...Yeah, sounded like it to me.\x02",
    )

    CloseMessageWindow()

    label("loc_3623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_365B")

    ChrTalk(    #193
        0x108,
        "#073FYes, he certainly did say Aina.\x02",
    )

    CloseMessageWindow()

    label("loc_365B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3690")

    ChrTalk(    #194
        0x104,
        "#032FMmmm... I can't let that go.\x02",
    )

    CloseMessageWindow()

    label("loc_3690")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #195
        0x11,
        "Yeah, that lovely lady in the guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x11,
        (
            "She's apparently a heavy drinker, but that's\x01",
            "no problem as long as I'm prepared!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "If I drink this medicine, I can invite her\x01",
            "out and survive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1020F#4PYou made that medicine to take\x01",
            "Aina on a date...?\x02\x03",

            "#1007FThat's both gutsy and...kinda pathetic...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385C")

    ChrTalk(    #199
        0x104,
        (
            "#032FStill, thinking about it, this might\x01",
            "be a golden opportunity.\x02\x03",

            "If we miss this moment, no one\x01",
            "might ever drink Aina under.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385C")


    ChrTalk(    #200
        0x103,
        (
            "#021FHa! I like the way you think.\x02\x03",

            "I'd love to see Aina get crushed under\x01",
            "the weight of her liquor for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x11,
        "Ohh! So you'll help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x11,
        (
            "I'd like you to find a way to\x01",
            "invite her out from the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A20")

    ChrTalk(    #203
        0x104,
        (
            "#035FHeh, a noble mission. We will endeavor\x01",
            "to do our utmost to aid you.\x02\x03",

            "#030F...Would meeting up at the bar work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x103,
        (
            "#020FYes, that should be fine.\x02\x03",

            "Once she hears there's drinking involved,\x01",
            "I'm sure Aina will show up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA2")

    label("loc_3A20")


    ChrTalk(    #205
        0x103,
        (
            "#020FAll right, then, let's have you wait at the bar.\x02\x03",

            "Once she hears there's drinking involved,\x01",
            "I'm sure Aina will show up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA2")

    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #206
        0x101,
        "#1020F#6PH-Hold it, Schera.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #207
        0x103,
        (
            "#525FNow, what's the problem?\x01",
            "We're already on board with it.\x02\x03",

            "We should always strive to go\x01",
            "that extra arge for our client. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1015F#6PRiiiiiight...\x02\x03",

            "#1007F(She just wants to drink, doesn't she...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        (
            "Man, I knew I was right to hire bracers!\x01",
            "You really care about your clients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x11,
        (
            "I'm heading to the bar, so see you\x01",
            "in a bit!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5D")

    ChrTalk(    #211
        0x104,
        "#031FYes, let us be off, brother!\x02",
    )

    CloseMessageWindow()

    label("loc_3C5D")


    def lambda_3C63():

        label("loc_3C63")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3C63")

    QueueWorkItem2(0xF8, 3, lambda_3C63)

    def lambda_3C74():

        label("loc_3C74")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3C74")

    QueueWorkItem2(0xF9, 3, lambda_3C74)

    def lambda_3C85():

        label("loc_3C85")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3C85")

    QueueWorkItem2(0x8, 3, lambda_3C85)

    def lambda_3C96():

        label("loc_3C96")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3C96")

    QueueWorkItem2(0x101, 3, lambda_3C96)

    def lambda_3CA7():
        OP_8E(0xFE, 0xFFFFC2C0, 0x0, 0xB1B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3CA7)
    OP_43(0x11, 0x0, 0x1, 0x8)
    WaitChrThread(0x103, 0x0)
    OP_44(0x101, 0x3)

    def lambda_3CD2():
        OP_6D(-14180, 0, 46960, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CD2)

    def lambda_3CEA():

        label("loc_3CEA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3CEA")

    QueueWorkItem2(0x103, 3, lambda_3CEA)
    WaitChrThread(0x11, 0x0)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x8, 0x3)
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D48")
    OP_62(0x104, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_43(0x104, 0x0, 0x1, 0x9)
    WaitChrThread(0x104, 0x0)
    SetChrFlags(0x104, 0x80)
    Jump("loc_3D4D")

    label("loc_3D48")

    Sleep(1000)

    label("loc_3D4D")

    OP_6D(-17110, 0, 44470, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D92")

    ChrTalk(    #212
        0x107,
        "#561FI hope Anton survives...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E47")

    label("loc_3D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC6")

    ChrTalk(    #213
        0x105,
        "#045FI hope Anton survives...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E47")

    label("loc_3DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DFA")

    ChrTalk(    #214
        0x108,
        "#075FHopefully he survives...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E47")

    label("loc_3DFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E47")

    ChrTalk(    #215
        0x106,
        (
            "#552FI'll be impressed if he can actually\x01",
            "out-drink Aina.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E47")


    ChrTalk(    #216
        0x8,
        (
            "#6P*sigh* That young man is far too\x01",
            "hasty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "#6PI still haven't even finished explaining\x01",
            "the medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1015F#6PAwww, I'm sure it'll be fine.\x02\x03",

            "I doubt that Aina will take up the\x01",
            "offer anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #219
        0x103,
        (
            "#021FJust you watch.\x02\x03",

            "Anyway, come by the bar if you're\x01",
            "interested.\x02\x03",

            "I'll drag Aina there later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0131   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_303A end

    def Function_8_3F9B(): pass

    label("Function_8_3F9B")

    OP_8E(0xFE, 0xFFFFC996, 0x0, 0xB748, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFCE00, 0x0, 0xB748, 0xBB8, 0x0)

    def lambda_3FC9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FC9)
    OP_8E(0xFE, 0xFFFFD364, 0x0, 0xB748, 0xBB8, 0x0)
    Return()

    # Function_8_3F9B end

    def Function_9_3FEA(): pass

    label("Function_9_3FEA")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFCE00, 0x0, 0xB748, 0x1388, 0x0)

    def lambda_4009():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4009)
    OP_8E(0xFE, 0xFFFFD364, 0x0, 0xB748, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_63(0x104)
    Return()

    # Function_9_3FEA end

    def Function_10_4032(): pass

    label("Function_10_4032")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 52230, 5000, 51080, 0)
    SetChrPos(0x103, 51500, 5000, 50530, 0)
    SetChrPos(0xF8, 52220, 5000, 49650, 0)
    SetChrPos(0xF9, 52230, 5000, 48630, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AC")
    SetChrPos(0xF9, 52220, 5000, 49650, 0)
    SetChrPos(0xF8, 52230, 5000, 48630, 0)

    label("loc_40AC")

    OP_6D(51850, 5000, 50700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #220
        0x101,
        (
            "#1002F#7POh, hey. See this chair?\x02\x03",

            "It's been placed just to the side in the chapel.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A1")

    ChrTalk(    #221
        0x105,
        (
            "#042FThey who sit by the side of the Goddess...\x02\x03",

            "Perhaps it means here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EC")

    label("loc_41A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4203")

    ChrTalk(    #222
        0x104,
        (
            "#032FThey who sit by the side of the Goddess...\x02\x03",

            "Perhaps this is the place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EC")

    label("loc_4203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_427B")

    ChrTalk(    #223
        0x106,
        (
            "#053FThey who sit by the side of the Goddess...\x02\x03",

            "#050FThis might be the place it's talking about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EC")

    label("loc_427B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42EC")

    ChrTalk(    #224
        0x108,
        (
            "#072FThey who sit by the side of the Goddess...\x02\x03",

            "Maybe this place is what it's talking about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EC")


    ChrTalk(    #225
        0x101,
        "#1002F#7PYeah... I'm gonna check it out.\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x3E8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x101,
        (
            "#1002F#7PI thought so...\x02\x03",

            "There's a card.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 32)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05'The second key is your next magical circle.'\x01",
            " 　　　　      ■■\x01",
            "              ■■■ 　　　　\x02\x03",

            "■ is something from the forest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #228
        0x101,
        (
            "#1001FAll right! Success!\x02\x03",

            "#1007FYeah, right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x103,
        (
            "#025FThis hint is like nothing we've\x01",
            "seen at this point.\x02\x03",

            "What on earth could it mean?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4561")

    ChrTalk(    #230
        0x107,
        (
            "#063FIt must be guiding us to a place\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4647")

    label("loc_4561")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45AE")

    ChrTalk(    #231
        0x105,
        (
            "#042FThis also looks like it's showing us\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4647")

    label("loc_45AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45FB")

    ChrTalk(    #232
        0x104,
        (
            "#032FThis also looks like it's showing us\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4647")

    label("loc_45FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4647")

    ChrTalk(    #233
        0x106,
        (
            "#050FMost likely this is showing us a place\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4647")


    ChrTalk(    #234
        0x101,
        (
            "#1015FConsidering the direction this\x01",
            "has taken until now, probably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x103,
        (
            "#020FYes, it's probably appropriate to assume that.\x02\x03",

            "Let's look around the city to see if there's\x01",
            "anything that resembles the hint.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x8)
    OP_28(0x77, 0x1, 0x10)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_10_4032 end

    SaveToFile()

Try(main)
