from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'R1503_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/R1503_1 ._SN',
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
        "Function_1_129F",         # 01, 1
        "Function_2_1563",         # 02, 2
        "Function_3_2329",         # 03, 3
        "Function_4_30DE",         # 04, 4
        "Function_5_310B",         # 05, 5
        "Function_6_3138",         # 06, 6
        "Function_7_3165",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, 1420, -10, 17940, 0)
    SetChrPos(0xF7, 2150, 10, 17460, 0)
    SetChrPos(0xF8, 1230, -10, 16430, 0)
    SetChrPos(0xF9, 2280, 0, 16219, 0)
    OP_6D(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x9,
        (
            "#4PSir, we can't handle these things\x01",
            "on our own!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#4PWe've got to contact headquarters for\x01",
            "reinforcements!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "They're that strong...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#4PYes, sir! I've never seen monsters\x01",
            "like these before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#4PGehenna, I wonder if they're even monsters,\x01",
            "really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F#6PUh...\x02\x03",

            "Hey, what's up?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2A0():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A0)
    Sleep(100)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #6
        0x8,
        "Uwaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "Who're you?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347")

    ChrTalk(    #8
        0x106,
        (
            "#551FYou know, I kinda wish people would start\x01",
            "recognizing the badge on sight.\x02\x03",

            "We're bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451")

    label("loc_347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AA")

    ChrTalk(    #9
        0x103,
        (
            "#027FOh, did you miss the emblem in\x01",
            "your panic?\x02\x03",

            "We're bracers, my good sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451")

    label("loc_3AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407")

    ChrTalk(    #10
        0x108,
        (
            "#070FThought you'd be able to tell\x01",
            "by the emblem.\x02\x03",

            "We're bracers, sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451")

    label("loc_407")


    ChrTalk(    #11
        0x101,
        (
            "#1000FUh, didn't you see the badge\x01",
            "on my chest?\x02\x03",

            "We're bracers, sir.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x8,
        "Bracers? Hmm...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D0")

    ChrTalk(    #13
        0x104,
        (
            "#030FYou brow seems furrowed by troubles,\x01",
            "my good man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB")

    label("loc_4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E")

    ChrTalk(    #14
        0x108,
        (
            "#072FYou seem to have some kind of problem.\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB")

    label("loc_51E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_554")

    ChrTalk(    #15
        0x103,
        "#027FSome kind of trouble, sir?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB")

    label("loc_554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_599")

    ChrTalk(    #16
        0x106,
        (
            "#052FWhat's up, exactly?\x01",
            "Some kind of trouble?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB")

    label("loc_599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DB")

    ChrTalk(    #17
        0x109,
        (
            "#1063FLooks like you've got problems,\x01",
            "officer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB")


    ChrTalk(    #18
        0x8,
        "Yes... you could say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Something completely unexpected has\x01",
            "occurred here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F#6PCompletely unexpected?\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "Well... you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "...Monsters have appeared in this\x01",
            "abandoned mine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(    #23
        0x109,
        (
            "#1068FUh. Maybe I'm just an ignorant man of the\x01",
            "cloth, but what's unexpected about that?\x02\x03",

            "Monster infestations occur all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_74F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D7")

    ChrTalk(    #24
        0x106,
        (
            "#052FWhat the hell's 'completely unexpected'\x01",
            "about that?\x02\x03",

            "Monster infestations occur almost daily\x01",
            "in some places.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_7D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85F")

    ChrTalk(    #25
        0x103,
        (
            "#023FThat doesn't strike me as particularly\x01",
            "unexpected.\x02\x03",

            "Monsters commonly infest abandoned or\x01",
            "uninhabited areas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_85F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C7")

    ChrTalk(    #26
        0x108,
        (
            "#073FWhat's unexpected about that?\x02\x03",

            "Monsters often infest areas abandoned\x01",
            "by man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_8C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(    #27
        0x104,
        (
            "#033FWhat is so strange about this?\x02\x03",

            "Monsters typically move into abandoned\x01",
            "places after people leave, no?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_945")


    ChrTalk(    #28
        0x8,
        "That's true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "You see, the monsters in here are...\x01",
            "not normal monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1002F#6PAre you guys sure you're not just, like,\x01",
            "overreacting or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#6PIt's true, I say! They're goddamn\x01",
            "insects made of metal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#6PThey sprang up out of nowhere all\x01",
            "throughout the mine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(    #33
        0x107,
        "#065FInsects...made of metal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1002F#6POkay, those DO sound kind of weird.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B22")

    ChrTalk(    #35
        0x105,
        (
            "#042FI see... I've never heard of a\x01",
            "monster like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7E")

    ChrTalk(    #36
        0x104,
        (
            "#035FHmm. I see.\x02\x03",

            "I cannot claim to know of any\x01",
            "monster such as that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_B7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(    #37
        0x108,
        (
            "#072FI see...\x02\x03",

            "I can't claim to know of any\x01",
            "metal insects myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")

    ChrTalk(    #38
        0x103,
        (
            "#022FI see...\x02\x03",

            "That doesn't sound like any monster\x01",
            "I'm familiar with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC4")

    ChrTalk(    #39
        0x106,
        (
            "#057FMmm, yeah, this could be bad.\x02\x03",

            "I sure as hell've never heard of 'metal\x01",
            "insects,' and you don't look like you're\x01",
            "lying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(    #40
        0x109,
        (
            "#1064FMetal...insects?\x02\x03",

            "Definitely never heard of anything\x01",
            "like that in a church book, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D38")


    ChrTalk(    #41
        0x8,
        (
            "My squad's mission is to ensure\x01",
            "local security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "Unfortunately, we don't have the kind\x01",
            "of firepower necessary to deal with\x01",
            "unknown monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "This is all a stone's throw from Ravennue\x01",
            "Village, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "We can't just ignore an infestation of\x01",
            "unknown creatures near an inhabited\x01",
            "area, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1015F#6PAaaand so we show up at just the\x01",
            "right time.\x02\x03",

            "#1007FI kinda think I see where this is going...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "I guess I'm pretty easy to read at this\x01",
            "point, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "Still, this is becoming fairly common,\x01",
            "isn't it? The guild and army helping one\x01",
            "another, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "I'm sorry to ask this of you,\x01",
            "but could you help us?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7D, 0x4, 0x4)
    OP_28(0x7D, 0x1, 0x1)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105D")

    ChrTalk(    #49
        0x101,
        (
            "#1006F#6PSure!\x02\x03",

            "It's our duty to investigate stuff\x01",
            "like this, after all.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_1282")

    label("loc_105D")


    ChrTalk(    #50
        0x101,
        (
            "#1015F#6PUm, I really wish we could help you,\x01",
            "but...\x02\x03",

            "I don't think we can right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "I... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "I suppose the request was rather sudden.\x01",
            "It's not unexpected, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F#6PUm... Sorry.\x02\x03",

            "If we get some time,\x01",
            "we'll come back to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "Please do, if you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "If you can't help, I'll have to convince\x01",
            "Command to send me some reinforcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "We'll need to take care of this before it\x01",
            "gets too serious... I just don't know if\x01",
            "I can convince them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006F#6PWe'll try to be back soon.\x02\x03",

            "See you later!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_28(0x7D, 0x1, 0x8000)

    label("loc_1282")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_8C(0x8, 90, 0)
    OP_8C(0x9, 270, 0)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_129F(): pass

    label("Function_1_129F")

    Fade(1000)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, 1420, -10, 17940, 0)
    SetChrPos(0xF7, 2150, 10, 17460, 0)
    SetChrPos(0xF8, 1230, -10, 16430, 0)
    SetChrPos(0xF9, 2280, 0, 16219, 0)
    OP_6D(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1373")

    ChrTalk(    #58
        0x8,
        "Bracers! Will you lend us your aid?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C0")

    label("loc_1373")


    ChrTalk(    #59
        0x8,
        "Bracers, you've returned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "How about it?\x01",
            "Will you lend us your aid?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145F")

    ChrTalk(    #61
        0x101,
        (
            "#1006F#6PSure!\x02\x03",

            "It's our duty to investigate stuff\x01",
            "like this, after all.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_1546")

    label("loc_145F")


    ChrTalk(    #62
        0x101,
        (
            "#1007F#6PNo, sorry. We only stopped by for a moment.\x01",
            "We're still, uh, pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1002F#6PI promise we'll come back if\x01",
            "we get some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "Please do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "Well, thank you for your concern,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1546")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_8C(0x8, 90, 0)
    OP_8C(0x9, 270, 0)
    EventEnd(0x0)
    Return()

    # Function_1_129F end

    def Function_2_1563(): pass

    label("Function_2_1563")


    ChrTalk(    #67
        0x8,
        "Thank you! We'll owe you after this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1010F#6PDon't worry about it, really.\x01",
            "It's an emergency.\x02\x03",

            "#1002FSo, let me make sure I understand\x01",
            "everything right...\x02\x03",

            "You basically want us to go in there and\x01",
            "exterminate the weird monsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "We want you to exterminate every one of\x01",
            "those unknown monsters dwelling in the\x01",
            "mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "They're VERY distinct. You shouldn't have any\x01",
            "trouble telling them apart from the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1002F#6PAll right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178E")

    ChrTalk(    #73
        0x107,
        (
            "#064FUm, do you know anything else about\x01",
            "these monsters?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)
    Jump("loc_1904")

    label("loc_178E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(    #74
        0x108,
        (
            "#072FCan you tell us anything else about\x01",
            "these monsters?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)
    Jump("loc_1904")

    label("loc_17E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184A")

    ChrTalk(    #75
        0x103,
        (
            "#022FI don't suppose you can tell us anything\x01",
            "else about these monsters?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Jump("loc_1904")

    label("loc_184A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(    #76
        0x106,
        (
            "#050FAnything else we should know about\x01",
            "these bugs?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    Jump("loc_1904")

    label("loc_189B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1904")

    ChrTalk(    #77
        0x104,
        (
            "#030FI do not suppose you have any other\x01",
            "information on our insectoid nemeses?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 400)

    label("loc_1904")


    ChrTalk(    #78
        0x9,
        "#6PLet's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "#6POne on one, they're not all that strong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#6PIt's the ones that show up every now and\x01",
            "then with different colors that you need\x01",
            "to watch out for.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #81
        0x101,
        "#1015F#6PDifferent colors?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #82
        0x9,
        "#6PYeah! They use somethin' LIKE arts, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#6PMan... Gehenna take me if they're like\x01",
            "any arts I've ever seen, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        "#1020F#6PUnknown arts? You're kidding, right?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4C")

    ChrTalk(    #85
        0x106,
        (
            "#057FMmph. Explains why the army guys were\x01",
            "so freaked when we showed up, at least.\x02\x03",

            "We'd better keep our eyes open\x01",
            "on this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE8")

    ChrTalk(    #86
        0x103,
        (
            "#022FThat does sound dangerous. I see why\x01",
            "you were so flustered when we arrived.\x02\x03",

            "We should keep our eyes open when\x01",
            "we're down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C78")

    ChrTalk(    #87
        0x108,
        (
            "#072FMmm... That does sound particularly\x01",
            "dangerous.\x02\x03",

            "We should pay close attention to the\x01",
            "monsters as we track them down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1C78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1B")

    ChrTalk(    #88
        0x104,
        (
            "#032FAh. That helps to explain the shock we\x01",
            "found our brave guardsmen in when we\x01",
            "arrived.\x02\x03",

            "We will need to be especially careful\x01",
            "here, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD1")

    ChrTalk(    #89
        0x109,
        (
            "#1068FYeeeahhh, I'd say that qualifies as\x01",
            "'unknown' in my book.\x02\x03",

            "#1063FLet's make sure we keep our eyes peeled\x01",
            "so they don't GET peeled out of their\x01",
            "sockets, hey?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF8")

    ChrTalk(    #90
        0x105,
        "#042FAbsolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E8B")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1C")

    ChrTalk(    #91
        0x107,
        "#062FR-Right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E8B")

    label("loc_1E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E43")

    ChrTalk(    #92
        0x104,
        "#030FAs you say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E8B")

    label("loc_1E43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6A")

    ChrTalk(    #93
        0x108,
        "#072FDefinitely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E8B")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8B")

    ChrTalk(    #94
        0x109,
        "#1063FAlways.\x02",
    )

    CloseMessageWindow()

    label("loc_1E8B")


    ChrTalk(    #95
        0x8,
        "That should be everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "Allow us to open the gate for you, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #97
        0x101,
        "#1002F#6PYeah, uh, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_1F0D():
        OP_8E(0x8, 0x500, 0x14, 0x58AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F0D)
    OP_8C(0x9, 0, 400)
    Sleep(100)

    def lambda_1F34():
        OP_8E(0x9, 0xAA0, 0x14, 0x58AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F34)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6E, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x8, -107910, 0, 19880, 225)
    SetChrPos(0x9, -108310, 10, 21740, 180)
    SetChrPos(0xA, -112120, -20, 21740, 180)
    SetChrPos(0x101, -110760, -10, 18000, 0)
    SetChrPos(0xF7, -109590, 30, 18000, 0)
    SetChrPos(0xF8, -110360, -10, 16780, 0)
    SetChrPos(0xF9, -109070, -20, 16780, 0)
    OP_6D(-108800, 30, 17820, 0)
    OP_4A(0xA, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #98
        0x8,
        "#6PWell, then...take care, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        "#6PCome back here if you need a break.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "#6PWe've got an orbment charging station here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(    #101
        0x101,
        (
            "#1006FThanks! That'll help for sure.\x02\x03",

            "Once we've exterminated all the target\x01",
            "monsters, we'll come back to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        "#6PPlease do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "#6PAidios' blessing be on you all.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2182")

    ChrTalk(    #104
        0x106,
        "#050FOn your go, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2222")

    label("loc_2182")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C1")

    ChrTalk(    #105
        0x103,
        "#022FCome on, then. We should get to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2222")

    label("loc_21C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F3")

    ChrTalk(    #106
        0x108,
        "#072FLet's get to it, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2222")

    label("loc_21F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2222")

    ChrTalk(    #107
        0x104,
        "#035FBy your lead, Estelle.\x02",
    )

    CloseMessageWindow()

    label("loc_2222")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #108
        0x101,
        "#1002F#6PYeah, let's go.\x02",
    )

    CloseMessageWindow()

    def lambda_224D():

        label("loc_224D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_224D")

    QueueWorkItem2(0x8, 1, lambda_224D)

    def lambda_225E():
        OP_6D(-109790, -40, 22610, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_225E)

    def lambda_2276():
        OP_8E(0x101, 0xFFFE4F58, 0xFFFFFFF6, 0x6464, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2276)
    Sleep(100)

    def lambda_2296():
        OP_8E(0xF7, 0xFFFE53EA, 0xFFFFFFF6, 0x6464, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2296)

    def lambda_22B1():
        OP_8E(0xF8, 0xFFFE50E8, 0xFFFFFFF6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_22B1)
    Sleep(100)

    def lambda_22D1():
        OP_8E(0xF9, 0xFFFE55F2, 0xFFFFFFF6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_22D1)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_28(0x7D, 0x4, 0x8)
    OP_28(0x7D, 0x1, 0x2)
    OP_28(0x7D, 0x1, 0x4)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1563 end

    def Function_3_2329(): pass

    label("Function_3_2329")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    SetChrPos(0x8, -108020, 30, 18910, 270)
    SetChrPos(0x9, -108310, 10, 21740, 180)
    SetChrPos(0xA, -112120, -20, 21740, 180)
    OP_6D(-109690, 20, 20450, 0)
    OP_67(0, 7330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x8, 255)
    Sleep(1000)
    OP_8C(0x8, 0, 400)
    OP_4A(0x8, 255)
    Sleep(500)
    OP_6D(-109010, 0, 23650, 1500)

    def lambda_23F9():

        label("loc_23F9")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_23F9")

    QueueWorkItem2(0x8, 1, lambda_23F9)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x1, 0x4)
    Sleep(150)
    OP_43(0xF7, 0x0, 0x1, 0x5)
    Sleep(100)
    OP_43(0xF8, 0x0, 0x1, 0x6)
    Sleep(150)
    OP_43(0xF9, 0x0, 0x1, 0x7)
    OP_6D(-109690, 20, 20450, 2500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_44(0x8, 0x1)

    ChrTalk(    #109
        0x8,
        "How goes it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1006F#6PYour 'insects' are all stomped!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250E")

    ChrTalk(    #111
        0x106,
        (
            "#051FI doubt you guys'll have much trouble\x01",
            "from here on out.\x02\x03",

            "We'll leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_250E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2579")

    ChrTalk(    #112
        0x103,
        (
            "#020FYou shouldn't have any more trouble\x01",
            "for now, sir.\x02\x03",

            "We'll leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_2579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E5")

    ChrTalk(    #113
        0x108,
        (
            "#070FThe mine shouldn't give you much more\x01",
            "trouble now.\x02\x03",

            "We'll leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_25E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2658")

    ChrTalk(    #114
        0x104,
        (
            "#030FYou may wipe your cares from your brow.\x02\x03",

            "We shall leave the rest in your capable\x01",
            "hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E4")

    label("loc_2658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E4")

    ChrTalk(    #115
        0x105,
        (
            "#040FYes, you shouldn't have any more trouble\x01",
            "here. For the moment, at least.\x02\x03",

            "We will leave the rest to the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E4")


    ChrTalk(    #116
        0x8,
        "You really did it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "Talk about a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1015F#6PIt is sort of a relief, I guess...\x02\x03",

            "#1003FStill, those 'monsters'...\x01",
            "They were obviously machines.\x02\x03",

            "Could this be the society's doing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2875")

    ChrTalk(    #119
        0x109,
        (
            "#1067FGambling's one thing I DON'T do...but if\x01",
            "I were a bettin' man, I'd put good money it.\x02\x03",

            "Still got no idea why they'd send those\x01",
            "things to a random place like this,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2990")

    label("loc_2875")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C8")

    ChrTalk(    #120
        0x104,
        (
            "#032FHmmm. It is something we cannot\x01",
            "discount at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2990")

    label("loc_28C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FF")

    ChrTalk(    #121
        0x108,
        "#074FThat's pretty likely, yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2990")

    label("loc_28FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(    #122
        0x103,
        "#022FIt wouldn't surprise me at this point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2990")

    label("loc_2941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2990")

    ChrTalk(    #123
        0x106,
        (
            "#053FYeah, given all the crazy stuff so far,\x01",
            "that's likely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2990")


    ChrTalk(    #124
        0x8,
        (
            "The society...? You mean the Society of\x01",
            "Ouroboros, the criminal organization we\x01",
            "were briefed on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "I see... So it's possible they were\x01",
            "behind this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1002F#6PYeah, I think so.\x02\x03",

            "We've fought them a number of times,\x01",
            "but they don't play by normal rules.\x02\x03",

            "You guys should be extra careful, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B4C")

    ChrTalk(    #127
        0x103,
        (
            "#022FThe guild is also investigating the\x01",
            "society.\x02\x03",

            "We'll be sure and let the army know\x01",
            "if we discover anything new.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D77")

    label("loc_2B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BC1")

    ChrTalk(    #128
        0x106,
        (
            "#050FThe guild's also going after the society.\x02\x03",

            "We find anything new,\x01",
            "we'll let the army know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D77")

    label("loc_2BC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C58")

    ChrTalk(    #129
        0x108,
        (
            "#072FThe Bracer Guild is also investigating\x01",
            "Ouroboros.\x02\x03",

            "If we discover anything new, we'll be\x01",
            "sure to pass it along to the army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D77")

    label("loc_2C58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CEA")

    ChrTalk(    #130
        0x104,
        (
            "#032FThe Society of Ouroboros are our foemen,\x01",
            "as well.\x02\x03",

            "Anything we discover about them\x01",
            "will be shared with the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D77")

    label("loc_2CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D77")

    ChrTalk(    #131
        0x109,
        (
            "#1063FOur little team is also hot on the trail\x01",
            "of the society.\x02\x03",

            "If we find anything, we'll be sure and\x01",
            "let the army know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D77")


    ChrTalk(    #132
        0x8,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "I will be sure and make a detailed report\x01",
            "to the border garrison about this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "I'll also make sure just compensation for\x01",
            "your help is transferred to your guild\x01",
            "branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006F#6PGreat! Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "Well, then, bracers.\x01",
            "Take care out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "Let us all make sure we don't\x01",
            "drop our watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "That's the only way to fight a foe who\x01",
            "stays in the shadows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1002F#6PYou too, sir.\x02\x03",

            "Good luck with the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "Aidios guide your steps, friends.\x02",
    )

    CloseMessageWindow()

    def lambda_2F65():

        label("loc_2F65")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2F65")

    QueueWorkItem2(0x8, 1, lambda_2F65)

    def lambda_2F76():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F76)
    Sleep(200)

    def lambda_2F89():
        OP_8E(0x101, 0xFFFE4FF8, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F89)

    def lambda_2FA4():
        OP_6D(-110030, 10, 15330, 4000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2FA4)
    Sleep(200)

    def lambda_2FC1():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2FC1)
    Sleep(250)

    def lambda_2FD4():
        OP_8E(0xF7, 0xFFFE4FF8, 0xA, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2FD4)

    def lambda_2FEF():
        OP_8C(0xF8, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2FEF)
    Sleep(200)

    def lambda_3002():
        OP_8E(0xF8, 0xFFFE5336, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3002)

    def lambda_301D():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_301D)
    Sleep(200)

    def lambda_3030():
        OP_8E(0xF9, 0xFFFE4C2E, 0xA, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3030)
    Sleep(1400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x0)
    OP_28(0x7D, 0x4, 0x10)
    OP_28(0x7D, 0x1, 0x10)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #141
        "Quest #2C[Mine Extermination] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_20(0x1388)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2329 end

    def Function_4_30DE(): pass

    label("Function_4_30DE")

    SetChrPos(0x101, -109630, -110, 25000, 180)
    OP_8E(0x101, 0xFFFE53C2, 0x28, 0x4A88, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_4_30DE end

    def Function_5_310B(): pass

    label("Function_5_310B")

    SetChrPos(0xF7, -110530, -110, 25700, 180)
    OP_8E(0xF7, 0xFFFE503E, 0x1E, 0x4CF4, 0x7D0, 0x0)
    OP_8C(0xF7, 90, 400)
    Return()

    # Function_5_310B end

    def Function_6_3138(): pass

    label("Function_6_3138")

    SetChrPos(0xF8, -109640, 30, 26310, 180)
    OP_8E(0xF8, 0xFFFE53B8, 0x1E, 0x4F56, 0x7D0, 0x0)
    OP_8C(0xF8, 135, 400)
    Return()

    # Function_6_3138 end

    def Function_7_3165(): pass

    label("Function_7_3165")

    SetChrPos(0xF9, -110560, 10, 27530, 180)
    OP_8E(0xF9, 0xFFFE5020, 0xA, 0x5208, 0x7D0, 0x0)
    OP_8C(0xF9, 135, 400)
    Return()

    # Function_7_3165 end

    SaveToFile()

Try(main)
